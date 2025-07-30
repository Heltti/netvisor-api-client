"""
netvisor.auth
~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from __future__ import absolute_import

import hashlib
import hmac
import time
import uuid
from datetime import UTC, datetime

from requests.auth import AuthBase


class NetvisorAuth(AuthBase):
    """
    Implements the custom authentication mechanism used by Netvisor.
    """

    ALGORITHM_HMACSHA256 = "HMACSHA256"
    ALGORITHM_MD5 = "MD5"

    VALID_LANGUAGES = ("EN", "FI", "SE")
    VALID_ALGORITHMS = (
        ALGORITHM_HMACSHA256,
        # MD5 hash is deprecated, Netvisor will soon drop support
        # https://support.netvisor.fi/fi/support/discussions/topics/77000290155
        ALGORITHM_MD5,
    )

    def __init__(
        self,
        sender,
        partner_id,
        partner_key,
        customer_id,
        customer_key,
        organization_id,
        language="FI",
        algorithm=ALGORITHM_HMACSHA256,
    ):
        self.sender = sender
        self.partner_id = partner_id
        self.partner_key = partner_key
        self.customer_id = customer_id
        self.customer_key = customer_key
        self.organization_id = organization_id
        self.language = language
        self.algorithm = algorithm.upper()
        if self.algorithm not in self.VALID_ALGORITHMS:
            raise ValueError(f"Algorithm must be one of {self.VALID_ALGORITHMS}")

    @property
    def language(self):
        """
        The language the API uses for the error messages.

        The language must be in ISO-3166 format.

        .. seealso:: :const:`VALID_LANGUAGES` for a list of accepted
        languages.
        """
        return self._language

    @language.setter
    def language(self, value):
        if value not in self.VALID_LANGUAGES:
            msg = "language must be one of {}".format(self.VALID_LANGUAGES)
            raise ValueError(msg)
        self._language = value

    @staticmethod
    def make_transaction_id():
        """
        Make a unique identifier for a Netvisor API request.

        Each request sent by the partner must use a unique identfier.
        Otherwise Netvisor API will raise :exc:`RequestNotUnique` error.
        """
        return uuid.uuid4().hex

    @staticmethod
    def make_timestamp():
        """
        Make a timestamp for a Netvisor API request.

        The timestamp is the current time in UTC as string in ANSI
        format with exactly 3 decimal places (.000).

        Example::

            >>> NetvisorAuth.make_timestamp()
            2025-06-26 20:09:50.000

        """

        return datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S.000")

    def md5_hash(self, url: str, timestamp: str, transaction_id: str):
        """
        Make a MD5 hash to authenticate a Netvisor API request.

        :param url:
            the URL where the request is sent to
        :param timestamp:
            a timestamp string (ANSI format, e.g. 'YYYY-MM-DD HH:MM:SS.000')
        :param transaction_id:
            a unique identifier for the request
        """

        parameters = [
            url,
            self.sender,
            self.customer_id,
            timestamp,
            self.language,
            self.organization_id,
            transaction_id,
            self.customer_key,
            self.partner_key,
        ]
        joined_parameters = b"&".join(
            p.encode("utf-8") if isinstance(p, str) else p for p in parameters
        )

        return hashlib.md5(joined_parameters).hexdigest()

    def hmac_hash(
        self, url: str, timestamp: str, transaction_id: str, timestamp_unix: int
    ):
        """
        Make a HMACSHA256 hash to authenticate a Netvisor API request.

        https://support.netvisor.fi/en/support/solutions/articles/77000557880-api-authentication#HMACSHA256-authentication

        :param url:
            the URL where the request is sent to
        :param timestamp:
            a timestamp string (ANSI format, e.g. 'YYYY-MM-DD HH:MM:SS.000')
        :param transaction_id:
            a unique identifier for the request
        :param timestamp_unix:
            The current time as a Unix timestamp
        """

        key = "{customer_key}&{partner_key}".format(
            customer_key=self.customer_key, partner_key=self.partner_key
        )

        msg = "&".join(
            [
                url,
                self.sender,
                self.customer_id,
                timestamp,
                self.language,
                self.organization_id,
                transaction_id,
                str(timestamp_unix),
                self.customer_key,
                self.partner_key,
            ]
        )

        return hmac.new(
            key=key.encode("ISO-8859-1"),
            msg=msg.encode("ISO-8859-1"),
            digestmod="sha256",
        ).hexdigest()

    def __call__(self, request):
        timestamp = self.make_timestamp()
        transaction_id = self.make_transaction_id()

        request.headers["X-Netvisor-Authentication-CustomerId"] = self.customer_id
        request.headers["X-Netvisor-Authentication-PartnerId"] = self.partner_id
        request.headers["X-Netvisor-Authentication-Sender"] = self.sender
        request.headers["X-Netvisor-Authentication-Timestamp"] = timestamp
        request.headers["X-Netvisor-Authentication-TransactionId"] = transaction_id
        request.headers["X-Netvisor-Authentication-MACHashCalculationAlgorithm"] = (
            self.algorithm
        )
        request.headers["X-Netvisor-Interface-Language"] = self.language
        request.headers["X-Netvisor-Organisation-Id"] = self.organization_id

        if self.algorithm == self.ALGORITHM_HMACSHA256:
            timestamp_unix = int(time.time())

            mac = self.hmac_hash(
                url=request.url,
                timestamp=timestamp,
                transaction_id=transaction_id,
                timestamp_unix=timestamp_unix,
            )

            request.headers["X-Netvisor-Authentication-TimestampUnix"] = str(
                timestamp_unix
            )
            request.headers["X-Netvisor-Authentication-UseHTTPResponseStatusCodes"] = (
                "1"
            )

        else:
            mac = self.md5_hash(
                url=request.url, timestamp=timestamp, transaction_id=transaction_id
            )

        request.headers["X-Netvisor-Authentication-MAC"] = mac

        return request

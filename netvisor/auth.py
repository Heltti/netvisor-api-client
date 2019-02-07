"""
    netvisor.auth
    ~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from __future__ import absolute_import

import datetime
import hashlib
import uuid

from requests.auth import AuthBase


class NetvisorAuth(AuthBase):
    """
    Implements the custom authentication mechanism used by Netvisor.
    """

    VALID_LANGUAGES = ('EN', 'FI', 'SE')

    def __init__(
            self, sender, partner_id, partner_key, customer_id, customer_key,
            organization_id, language='FI'
    ):
        self.sender = sender
        self.partner_id = partner_id
        self.partner_key = partner_key
        self.customer_id = customer_id
        self.customer_key = customer_key
        self.organization_id = organization_id
        self.language = language

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
            msg = 'language must be one of {}'.format(self.VALID_LANGUAGES)
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
        format.

        Example::

            >>> NetvisorAuth.make_timestamp()
            2008-07-24 15:49:12.221

        """
        now = datetime.datetime.utcnow()
        return now.isoformat(' ')[:-3]

    def make_mac(self, url, timestamp, transaction_id):
        """
        Make a MAC code to authenticate a Netvisor API request.

        :param url:
            the URL where the request is sent to
        :param timestamp:
            a timestamp returned by :meth:`make_timestamp`
        :param transaction_id:
            a unique identifier returned by :meth:`make_transaction_id`
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
        joined_parameters = b'&'.join(
            p.encode('utf-8') if isinstance(p, str) else p
            for p in parameters
        )
        return hashlib.md5(joined_parameters).hexdigest()

    def __call__(self, r):
        timestamp = self.make_timestamp()
        transaction_id = self.make_transaction_id()
        mac = self.make_mac(r.url, timestamp, transaction_id)

        r.headers['X-Netvisor-Authentication-CustomerId'] = self.customer_id
        r.headers['X-Netvisor-Authentication-MAC'] = mac
        r.headers['X-Netvisor-Authentication-PartnerId'] = self.partner_id
        r.headers['X-Netvisor-Authentication-Sender'] = self.sender
        r.headers['X-Netvisor-Authentication-Timestamp'] = timestamp
        r.headers['X-Netvisor-Authentication-TransactionId'] = transaction_id
        r.headers['X-Netvisor-Interface-Language'] = self.language
        r.headers['X-Netvisor-Organisation-ID'] = self.organization_id

        return r

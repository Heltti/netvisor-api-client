import datetime
import hashlib
import hmac
import time
import uuid

import pytest
from flexmock import flexmock
from freezegun import freeze_time

from netvisor_api_client.auth import NetvisorAuth


def make_auth(
    sender="Testiclient",
    partner_id="xxx_yyy",
    partner_key="07f94228d149a96b2f25e3edad55096e",
    customer_id="Integraatiokayttajan tunnus",
    customer_key="7cd680e89e880553358bc07cd28b0ee2",
    organization_id="1967543-8",
    algorithm=NetvisorAuth.ALGORITHM_HMACSHA256,
    **kwargs,
):
    return NetvisorAuth(
        sender,
        partner_id,
        partner_key,
        customer_id,
        customer_key,
        organization_id,
        algorithm=algorithm,
        **kwargs,
    )


@pytest.fixture
def auth():
    return make_auth()


class TestNetvisorAuth(object):
    REFERENCE_DATETIME = datetime.datetime(2024, 1, 1, 12, 0, 0)
    REFERENCE_TIMESTAMP = REFERENCE_DATETIME.strftime("%Y-%m-%d %H:%M:%S.000")
    REFERENCE_TIME = int(time.mktime(REFERENCE_DATETIME.timetuple()))

    @pytest.fixture
    def http_request(self, request):
        auth = NetvisorAuth(
            sender="Testiclient",
            partner_id="xxx_yyy",
            partner_key="07f94228d149a96b2f25e3edad55096e",
            customer_id="Integraatiokayttajan tunnus",
            customer_key="7cd680e89e880553358bc07cd28b0ee2",
            organization_id="1967543-8",
        )

        # Freeze time for easier testing
        with freeze_time(self.REFERENCE_TIMESTAMP):
            flexmock(time).should_receive("time").and_return(self.REFERENCE_TIME)

            url = "https://integrationdemo.netvisor.fi/accounting.nv"
            r = flexmock(headers={}, url=url, method="POST")

            return auth(r), auth, url

    def test_constructor_sets_sender(self, auth):
        assert auth.sender == "Testiclient"

    def test_constructor_sets_partner_id(self, auth):
        assert auth.partner_id == "xxx_yyy"

    def test_constructor_sets_partner_key(self, auth):
        assert auth.partner_key == "07f94228d149a96b2f25e3edad55096e"

    def test_constructor_sets_customer_id(self, auth):
        assert auth.customer_id == "Integraatiokayttajan tunnus"

    def test_constructor_sets_customer_key(self, auth):
        assert auth.customer_key == "7cd680e89e880553358bc07cd28b0ee2"

    def test_constructor_sets_organization_id(self, auth):
        assert auth.organization_id == "1967543-8"

    def test_constructor_sets_default_language(self, auth):
        assert auth.language == "FI"

    def test_constructor_sets_language(self, auth):
        auth = make_auth(language="EN")
        assert auth.language == "EN"

    @pytest.mark.parametrize(
        ("language", "valid"),
        [
            ("FI", True),
            ("EN", True),
            ("SE", True),
            ("NO", False),
            ("FR", False),
            ("", False),
            (None, False),
        ],
    )
    def test_validates_language(self, auth, language, valid):
        if valid:
            auth.language = language
        else:
            with pytest.raises(ValueError) as exc_info:
                auth.language = language
            msg = str(exc_info.value)
            assert msg == "language must be one of ('EN', 'FI', 'SE')"

    def test_adds_sender_header_to_request(self, http_request):
        result, _, _ = http_request

        assert result.headers["X-Netvisor-Authentication-Sender"] == "Testiclient"

    def test_adds_customer_id_header_to_request(self, http_request):
        result, _, _ = http_request

        assert (
            result.headers["X-Netvisor-Authentication-CustomerId"]
            == "Integraatiokayttajan tunnus"
        )

    def test_adds_timestamp_header_to_request(self, http_request):
        result, _, _ = http_request

        assert (
            result.headers["X-Netvisor-Authentication-Timestamp"]
            == self.REFERENCE_TIMESTAMP
        )

    def test_adds_language_header_to_request(self, http_request):
        result, _, _ = http_request

        assert result.headers["X-Netvisor-Interface-Language"] == "FI"

    def test_adds_organization_id_header_to_request(self, http_request):
        result, _, _ = http_request

        assert result.headers["X-Netvisor-Organisation-Id"] == "1967543-8"

    def test_adds_partner_id_header_to_request(self, http_request):
        result, _, _ = http_request

        assert result.headers["X-Netvisor-Authentication-PartnerId"] == "xxx_yyy"

    def test_make_transaction_id_uses_uuid(self, auth):
        fake_uuid = flexmock(hex="123456")
        flexmock(uuid).should_receive("uuid4").and_return(fake_uuid).once()
        assert auth.make_transaction_id() == "123456"

    def test_make_timestamp_returns_current_time_in_isoformat(self, auth):
        with freeze_time("2009-01-12 15:49:12.221"):
            assert auth.make_timestamp() == "2009-01-12 15:49:12.000"

    def test_hmacsha256_headers_and_mac(self):
        auth = NetvisorAuth(
            sender="Testiclient",
            partner_id="xxx_yyy",
            partner_key="partnerkey",
            customer_id="customerid",
            customer_key="customerkey",
            organization_id="orgid",
            algorithm="HMACSHA256",
        )

        with freeze_time(self.REFERENCE_TIMESTAMP):
            flexmock(time).should_receive("time").and_return(self.REFERENCE_TIME)

            url = "https://integrationdemo.netvisor.fi"
            timestamp = auth.make_timestamp()

            # Check headers
            r = flexmock(headers={}, url=url, method="POST")
            result = auth(r)

            transaction_id = result.headers["X-Netvisor-Authentication-TransactionId"]

            hmac_key = "customerkey&partnerkey"
            hmac_msg = "&".join(
                [
                    url,
                    "Testiclient",
                    "customerid",
                    timestamp,
                    "FI",
                    "orgid",
                    transaction_id,
                    str(self.REFERENCE_TIME),
                    "customerkey",
                    "partnerkey",
                ]
            )
            expected_mac = hmac.new(
                key=hmac_key.encode("ISO-8859-1"),
                msg=hmac_msg.encode("ISO-8859-1"),
                digestmod="sha256",
            ).hexdigest()

            assert (
                result.headers["X-Netvisor-Authentication-CustomerId"] == "customerid"
            )
            assert result.headers["X-Netvisor-Authentication-MAC"] == expected_mac
            assert result.headers["X-Netvisor-Authentication-Sender"] == "Testiclient"
            assert result.headers["X-Netvisor-Authentication-Timestamp"] == timestamp
            assert result.headers["X-Netvisor-Interface-Language"] == "FI"
            assert result.headers["X-Netvisor-Organisation-Id"] == "orgid"
            assert (
                result.headers["X-Netvisor-Authentication-MACHashCalculationAlgorithm"]
                == "HMACSHA256"
            )
            assert result.headers["X-Netvisor-Authentication-TimestampUnix"] == str(
                self.REFERENCE_TIME
            )
            assert (
                result.headers["X-Netvisor-Authentication-UseHTTPResponseStatusCodes"]
                == "1"
            )

    def test_md5_legacy_algorithm(self):
        url = "https://integrationdemo.netvisor.fi"
        transaction_id = "txid123"

        auth_md5 = NetvisorAuth(
            sender="A",
            partner_id="B",
            partner_key="C",
            customer_id="D",
            customer_key="E",
            organization_id="F",
            algorithm="MD5",
        )
        params_md5 = [
            url,
            "A",
            "D",
            self.REFERENCE_TIMESTAMP,
            "FI",
            "F",
            transaction_id,
            "E",
            "C",
        ]
        joined_md5 = b"&".join(p.encode("utf-8") for p in params_md5)
        expected_md5 = hashlib.md5(joined_md5).hexdigest()

        assert (
            auth_md5.md5_hash(url, self.REFERENCE_TIMESTAMP, transaction_id)
            == expected_md5
        )

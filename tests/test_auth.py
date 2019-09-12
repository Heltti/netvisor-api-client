import uuid

import pytest
from flexmock import flexmock
from freezegun import freeze_time


def make_auth(
        sender='Testiclient',
        partner_id='xxx_yyy',
        partner_key='07f94228d149a96b2f25e3edad55096e',
        customer_id='Integraatiokayttajan tunnus',
        customer_key='7cd680e89e880553358bc07cd28b0ee2',
        organization_id='1967543-8',
        **kwargs
):
    from netvisor_api_client.auth import NetvisorAuth

    return NetvisorAuth(
        sender,
        partner_id,
        partner_key,
        customer_id,
        customer_key,
        organization_id,
        **kwargs
    )


@pytest.fixture
def auth():
    return make_auth()


class TestNetvisorAuth(object):
    @pytest.fixture
    def http_request(self, request, auth):
        (
            flexmock(auth)
                .should_receive('make_transaction_id')
                .and_return('123456')
        )
        (
            flexmock(auth)
                .should_receive('make_timestamp')
                .and_return('2009-01-12 15:49:12.221')
        )
        (
            flexmock(auth)
                .should_receive('make_mac')
                .with_args(
                'http://integrationdemo.netvisor.fi/accounting.nv',
                '2009-01-12 15:49:12.221',
                '123456'
            )
                .and_return('6b2783906969630c1b6649bf5b0e6620')
        )
        r = flexmock(
            headers={},
            url='http://integrationdemo.netvisor.fi/accounting.nv'
        )
        return auth(r)

    def test_constructor_sets_sender(self, auth):
        assert auth.sender == 'Testiclient'

    def test_constructor_sets_partner_id(self, auth):
        assert auth.partner_id == 'xxx_yyy'

    def test_constructor_sets_partner_key(self, auth):
        assert auth.partner_key == '07f94228d149a96b2f25e3edad55096e'

    def test_constructor_sets_customer_id(self, auth):
        assert auth.customer_id == 'Integraatiokayttajan tunnus'

    def test_constructor_sets_customer_key(self, auth):
        assert auth.customer_key == '7cd680e89e880553358bc07cd28b0ee2'

    def test_constructor_sets_organization_id(self, auth):
        assert auth.organization_id == '1967543-8'

    def test_constructor_sets_default_language(self, auth):
        assert auth.language == 'FI'

    def test_constructor_sets_language(self, auth):
        auth = make_auth(language='EN')
        assert auth.language == 'EN'

    @pytest.mark.parametrize(
        ('language', 'valid'),
        [
            ('FI', True),
            ('EN', True),
            ('SE', True),
            ('NO', False),
            ('FR', False),
            ('', False),
            (None, False),
        ]
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
        assert (
                http_request.headers['X-Netvisor-Authentication-Sender'] ==
                'Testiclient'
        )

    def test_adds_customer_id_header_to_request(self, http_request):
        assert (
                http_request.headers['X-Netvisor-Authentication-CustomerId'] ==
                'Integraatiokayttajan tunnus'
        )

    def test_adds_timestamp_header_to_request(self, http_request):
        assert (
                http_request.headers['X-Netvisor-Authentication-Timestamp'] ==
                '2009-01-12 15:49:12.221'
        )

    def test_adds_language_header_to_request(self, http_request):
        assert http_request.headers['X-Netvisor-Interface-Language'] == 'FI'

    def test_adds_organization_id_header_to_request(self, http_request):
        assert (
                http_request.headers['X-Netvisor-Organisation-ID'] == '1967543-8'
        )

    def test_adds_transaction_id_header_to_request(self, http_request):
        assert (
                http_request.headers['X-Netvisor-Authentication-TransactionId'] ==
                '123456'
        )

    def test_adds_mac_header_to_request(self, http_request):
        assert (
                http_request.headers['X-Netvisor-Authentication-MAC'] ==
                '6b2783906969630c1b6649bf5b0e6620'
        )

    def test_adds_partner_id_header_to_request(self, http_request):
        assert (
                http_request.headers['X-Netvisor-Authentication-PartnerId'] ==
                'xxx_yyy'
        )

    def test_make_transaction_id_uses_uuid(self, auth):
        fake_uuid = flexmock(hex='123456')
        flexmock(uuid).should_receive('uuid4').and_return(fake_uuid).once()
        assert auth.make_transaction_id() == '123456'

    def test_make_timestamp_returns_current_time_in_isoformat(self, auth):
        with freeze_time('2009-01-12 15:49:12.221'):
            assert auth.make_timestamp() == '2009-01-12 15:49:12.221'

    def test_make_mac(self, auth):
        mac = auth.make_mac(
            'http://integrationdemo.netvisor.fi/accounting.nv',
            '2009-01-12 15:49:12.221',
            '123456'
        )
        assert mac == '6b2783906969630c1b6649bf5b0e6620'

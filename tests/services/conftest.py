import pytest
from responses import RequestsMock


@pytest.fixture
def netvisor():
    from netvisor import Netvisor
    kwargs = dict(
        sender='Test client',
        partner_id='xxx_yyy',
        partner_key='E2CEBB1966C7016730C70CA92CBB93DD',
        customer_id='xx_yyyy_zz',
        customer_key='7767899D6F5FB333784A2520771E5871',
        organization_id='1967543-8',
        language='EN'
    )
    return Netvisor(host='http://koulutus.netvisor.fi', **kwargs)


@pytest.yield_fixture(autouse=True)
def responses():
    r = RequestsMock()
    with r:
        yield r

import pytest
import os

from modules import nasa_restapi, testData

Nasa_Api = None

@pytest.fixture(scope="module", autouse=True)
def initialized_nasa_rstapi():
    """Connect to db before testing, disconnect after."""
    global Nasa_Api
    Nasa_Api = nasa_restapi.NasaRestApi(os.environ["ApiKey"])
    yield

@pytest.mark.parametrize('params', testData.positive_test_data())
def test_earth_get_positive(params):
    """"""
    result = Nasa_Api.GetEarthImagery(params)
    #assert result["success"]
    assert result["status_code"] == 200
    #TODO check the text is image


@pytest.mark.parametrize('params', testData.negative_test_data())
def test_earth_get_negative(params):
    """"""
    result = Nasa_Api.GetEarthImagery(params)
    assert not result["success"]
    assert result["status_code"] != 200
    #TODO check the text is not image
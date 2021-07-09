import pytest
import os
from http import HTTPStatus

from modules import testData
from modules.nasa import nasa_restapi

@pytest.fixture
def get_nasa_api():
    return nasa_restapi.NasaRestApi(os.environ["ApiKey"])

@pytest.mark.parametrize('params', testData.positive_earth_imagery_get_test_data())
def test_earth_get_positive(get_nasa_api, params):
    """Verify planetary/earth with right parameters"""
    result = get_nasa_api.GetEarthImagery(params)
    assert result["status_code"] == HTTPStatus.OK
    #TODO check the text is image


@pytest.mark.parametrize('params', testData.negative_earth_imageryget_test_data())
def test_earth_get_negative(get_nasa_api, params):
    """Verify planetary/earth with negative parameters"""
    result = get_nasa_api.GetEarthImagery(params)
    assert not result["success"] and result["status_code"] != HTTPStatus.OK
    #TODO check the text is not image


@pytest.mark.parametrize('params', testData.positive_earth_imagery_get_test_data())
def test_earth_get_without_apiKey(params):
    """Verify planetary/earth request without api key"""
    nasa_api = nasa_restapi.NasaRestApi(api_key=None)
    result = nasa_api.GetEarthImagery(params)
    assert not result["success"] and result["status_code"] == HTTPStatus.FORBIDDEN

#TODO tests for verifying an image depends from dim, date in metadata
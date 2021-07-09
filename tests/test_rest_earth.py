import pytest
import os
from http import HTTPStatus

from modules import nasa_restapi, testData, test_functions as tf

NASA_API = None #global value

@pytest.fixture(scope="module", autouse=True)
def initialized_nasa_rest_obj():
    """initialize nasa api class"""
    global NASA_API
    NASA_API = nasa_restapi.NasaRestApi(os.environ["ApiKey"])
    yield

@pytest.mark.parametrize('params', testData.positive_earth_get_test_data())
def test_earth_get_positive(params):
    """Verify planetary/earth with right parameters"""
    result = NASA_API.GetEarthImagery(params)
    assert result["status_code"] == HTTPStatus.OK
    assert tf.is_Image(result["text"])


@pytest.mark.parametrize('params', testData.negative_earth_get_test_data())
def test_earth_get_negative(params):
    """Verify planetary/earth with negative parameters"""
    result = NASA_API.GetEarthImagery(params)
    assert not result["success"] and result["status_code"] != HTTPStatus.OK
    #TODO check the text is not image


@pytest.mark.parametrize('params', testData.positive_earth_get_test_data())
def test_earth_get_without_apiKey(params):
    """Verify planetary/earth request without api key"""
    nasa_api = nasa_restapi.NasaRestApi(api_key=None)
    result = nasa_api.GetEarthImagery(params)
    assert not result["success"] and result["status_code"] == HTTPStatus.FORBIDDEN

#TODO tests for verifying an image: dim, date in metadata
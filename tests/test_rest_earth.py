import pytest
import os

from modules import nasa_restapi

ApiKey = os.environ["ApiKey"]

def test_earth_get_positive():
    """"""
    nasa_api = nasa_restapi.NasaRestApi(ApiKey)
    #result = nasa_api.GetEarthImagery({"lon": 100.75,"lat": 1.5, "date": "2014-02-01"})
    result = nasa_api.GetEarthImagery()

    assert True
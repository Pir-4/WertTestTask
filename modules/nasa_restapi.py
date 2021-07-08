import requests
from modules import nasa_costants as NC

class NasaRestApi:
    """"""
    requests = {"GET": requests.get}

    def __init__(self, api_key=None):
        self.api_key = api_key

    def Request(self, rtype, categories, endPointName, params=None):
        """"""
        mainUrl = self.__GetUrl(categories, endPointName)
        params = params or {}
        params["api_key"] = self.api_key

        response = self.requests[rtype.upper()](mainUrl, params)
        result = {"status_code": response.status_code,
                  "reason": response.reason,
                  "text": response.text,
                  "success": response.ok}
        return result

    def GetEarthImagery(self, filterDict=None):
        """"""
        return self.Request("Get", [NC.PLANET_CATEGORY, NC.EARTH], NC.imagery, params=filterDict)

    def __GetUrl(self, categories, endPointName):
        """"""
        urlParts = [NC.MAIN_URL]
        urlParts += categories if isinstance(categories, list) else [categories]
        urlParts += [endPointName]
        return "/".join(urlParts)



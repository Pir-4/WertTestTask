import requests
from modules import nasa_costants as NC

class NasaRestApi:
    """ Implement NSA Rest API"""
    requests = {"GET": requests.get}

    def __init__(self, api_key=None):
        """ Init class

        :param api_key:api key which was given from https://api.nasa.gov/
        :rtype: str
        """
        self.api_key = api_key

    def Request(self, req_type, categories, params=None):
        """ Send request

        :param req_type: request type: GET
        :type req_type: str
        :param categories: parts of URL to endpoint
        :type categories: list
        :param params: parameters for request
        :type params: dict
        :return: request result: status_code, reason, text, success
        :rtype: dict
        """
        request_url = self.__GetUrl(categories)
        params = params or {}
        if self.api_key and not params.get("api_key"):
            params["api_key"] = self.api_key

        response = self.requests[req_type.upper()](request_url, params)
        result = {"status_code": response.status_code,
                  "reason": response.reason,
                  "text": response.text,
                  "success": response.ok}
        return result

    def GetEarthImagery(self, params=None):
        """ GET request to /planetary/earth/imagery

        :param params: params for request
        :type params dict
        :return: request result: status_code, reason, text, success
        :rtype: dict
        """
        return self.Request("GET", [NC.PLANET_CATEGORY, NC.EARTH, NC.IMAGERY], params=params)

    def __GetUrl(self, url_parts, main_url=NC.MAIN_URL):
        """ Get final URL

        :param url_parts: list of parts of path
        :type url_parts: list
        :param main_url: main part of URL
        :type main_url: str
        :return: full request URL
        :rtype: str
        """
        join_url_parts = [main_url]
        join_url_parts += url_parts if isinstance(url_parts, list) else [url_parts]
        return "/".join(join_url_parts)



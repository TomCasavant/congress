import requests
import requests.packages
from typing import Dict, Union
#from .exceptions import *
from .models import Result
import logging
from json import JSONDecodeError
from io import BytesIO

class RestAdapter:
    """
    https://api.congress.gov/v3/
    """
    def __init__(self, hostname: str, api_key: str = "", ver: str = "v3", ssl_verify: bool = True, logger: logging.Logger = None):
        self.url = f"https://{hostname}/{ver}/"
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        self._logger = logger or logging.getLogger(__name__)
        if not ssl_verify:
            requests.packages.urllib3.disable_warnings()

    def get(self, endpoint: str, ep_params: Dict = {}) -> Result:
        """
        """
        result = self._do(http_method="GET", endpoint=endpoint, ep_params=ep_params)
        return result

    def _do(self, http_method: str, endpoint: str, ep_params: Dict = {}, data: Dict = {}) -> Result:
        full_url = endpoint if endpoint.startswith('http') else self.url + endpoint
        headers = { "X-API-Key": self._api_key }
        ep_params = {k: v for k, v in ep_params.items() if v is not None}
        try:
            response = requests.request(
                method=http_method,
                url=full_url,
                verify=self._ssl_verify,
                headers=headers,
                params=ep_params,
                json=data,
            )
        except (ValueError, JSONDecodeError) as e:
            raise Exception(f"Failed to decode JSON: {e}") from e
        

        if 299 >= response.status_code >= 200:
            data_out = response.json()
            result = Result(
                status_code=response.status_code,
                message=response.reason,
                data=data_out
            )

            return result

        print(response)


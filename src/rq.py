import serde
import requests
import typing
import re
import html


class InvalidAuthenticationMode(Exception):
    def __init__(self, mode):
        print(f"Invalid authentication mode '{mode}")


class RequiresOauth(Exception):
    def __init__(self):
        print("\033[91mThis method cannot be called using a public api_key!")
        print("As it is user-specific, you must perform the Oauth flow!")
        print("See: https://www.etsy.com/developers/documentation/getting_started/oauth\033[0m")


class InvalidURIParams(Exception):
    def __init__(self, uri: str, expected: list, given: list):
        print(f"\033[91mInvalid URI params for {uri}!")
        print(f"Expected: {expected}")
        print(f"Found: {given}")


class EtsyResponse:
    """
    The wrapper for the etsy response.
    """

    def __init__(self, response: requests.Response):
        self.response: requests.Response = response

    def ok(self):
        return self.response.status_code == 200


class EtsyRequester:
    """
    Makes requests, handles authentication and such and such...
    """
    def __init__(self,
                 auth_mode: str = "api_key",
                 api_key: typing.Union[None, str] = None,
                 api_base_url: str = "https://openapi.etsy.com/v2"
                 ):

        self.session: requests.Session = requests.Session()
        self.api_base_url = api_base_url

        if auth_mode == "api_key":
            self.api_key = api_key
            self.mode = auth_mode
            self.session.params.update(api_key=api_key)
        elif auth_mode == "oauth":
            pass
        else:
            raise InvalidAuthenticationMode(auth_mode)

    def make_request(self,
                     uri: str,
                     method: str,
                     uri_params: list = None,
                     query_params: dict = None,
                     data: dict = None
                     ) -> EtsyResponse:

        required_uri_params = re.findall(':(\w+)(?:\/|$)', uri)
        if len(required_uri_params) != len(uri_params):
            raise InvalidURIParams(uri, expected=required_uri_params, given=uri_params)

        if method not in ["GET", "PUT", "POST", "PATCH", "DELETE"]:
            raise ValueError(f"Invalid HTTP method: {method}, are you manually running make_request?")

        uri_params_dict = dict()
        for _ in range(0, len(required_uri_params)-1):
            uri_params_dict.update(**{required_uri_params[_]: uri_params[_]})

        for uri_param_key, uri_param_value in uri_params_dict.items():
            uri = uri.replace(f":{uri_param_key}", html.escape(uri_param_value))

        response = self.session.request(
            method=method,
            url=f"{self.api_base_url}{uri}",
            params=query_params,
            json=data
        )
        return EtsyResponse(response)

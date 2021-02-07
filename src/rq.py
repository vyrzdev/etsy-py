import requests
import requests_oauthlib
import typing
import re
import html
import dataclasses


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


@dataclasses.dataclass
class EtsyOauthCredentials:
    client_key: str
    client_secret: str
    resource_owner_key: str
    resource_owner_secret: str


class EtsyRequester:
    """
    Makes requests, handles authentication and such and such...
    """
    def __init__(self,
                 auth_mode: str = "api_key",
                 api_key: typing.Union[None, str] = None,
                 oauth_credentials: typing.Union[EtsyOauthCredentials, None] = None,
                 api_base_url: str = "https://openapi.etsy.com/v2"
                 ):

        self.api_base_url = api_base_url
        self.auth_mode = auth_mode

        if auth_mode == "api_key":
            self.session: requests.Session = requests.Session()
            if api_key is None:
                print("Warning: Etsy api_key expected as kwarg of Requester when using api_key authentication mode!")
            self.api_key = api_key
            self.session.params.update(api_key=api_key)
        elif auth_mode == "oauth":
            if oauth_credentials is None:
                print("Warning: oauth_credentials of type rq.EtsyOauthCredentials expected as kwarg of Requester when using oauth_1 authentication mode!")
            self.session: requests_oauthlib.OAuth1Session = requests_oauthlib.OAuth1Session(
                client_key=oauth_credentials.client_key,
                client_secret=oauth_credentials.client_secret,
                resource_owner_key=oauth_credentials.resource_owner_key,
                resource_owner_secret=oauth_credentials.resource_owner_secret
            )
            # TODO: Test PUT/POST requests with Oauth auth mode.
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
        for _ in range(0, len(required_uri_params)):
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

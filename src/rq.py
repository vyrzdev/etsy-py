import serde
import requests
import typing


class InvalidAuthenticationMode(Exception):
    def __init__(self, mode):
        print(f"Invalid authentication mode '{mode}")


class RequiresOauth(Exception):
    def __init__(self):
        print("\033[91m This method cannot be called using a public api_key!")
        print("As it is user-specific, you must perform the Oauth flow!")
        print("See: https://www.etsy.com/developers/documentation/getting_started/oauth\033[0m")

class EtsyResponse:
    """
    The wrapper for the etsy response.
    """
    pass


class EtsyRequester:
    """
    Makes requests, handles authentication and such and such...
    """
    def __init__(self,
                 auth_mode: str = "api_key",
                 api_key: typing.Union[None, str] = None,
                 ):

        self.session: requests.Session = requests.Session()

        if auth_mode == "api_key":
            self.api_key = api_key
            self.mode = auth_mode
            self.session.params.update(api_key=api_key)
        elif auth_mode == "oauth":
            pass
        else:
            raise InvalidAuthenticationMode(auth_mode)

    def make_request(self, **kwargs):

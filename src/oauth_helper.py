import requests_oauthlib
import typing
import urllib.parse
from .rq import EtsyOauthCredentials


class OauthFlowFailed(Exception):
    def __init__(self, content):
        print("Oauth flow failed?")
        print(content)


class EtsyOauthHelper:
    def __init__(self, api_key: str, shared_secret: str, api_base_url: str = "https://openapi.etsy.com/v2", debug: bool = False):
        self.api_key = api_key
        self.debug = debug
        self.api_base_url = api_base_url
        self.shared_secret = shared_secret
        self.session: requests_oauthlib.OAuth1Session = requests_oauthlib.OAuth1Session(api_key, client_secret=shared_secret)

    def get_login_url(self,
                      permission_scopes: typing.List[str],
                      redirect_uri: typing.Union[str, None] = None
                      ) -> typing.Tuple[str, str, str]:

        if self.debug:
            if redirect_uri is None:
                print("Using manual verifier code based flow!")
            else:
                print("Using redirect_uri based flow!")

        permission_scopes_str = " ".join(permission_scopes)

        params = dict()
        params["scope"] = permission_scopes_str
        if redirect_uri is not None:
            params["oauth_callback"] = redirect_uri

        response = self.session.request(
            method="GET",
            url=f"{self.api_base_url}/oauth/request_token",
            params=params
        )

        if response.status_code != 200:
            raise OauthFlowFailed(response.content)

        login_url: str = urllib.parse.unquote(response.content.decode())[10:]
        url_parameters: dict = urllib.parse.parse_qs(urllib.parse.urlsplit(login_url).query)
        temp_oauth_token: str = url_parameters.get("oauth_token")[0]
        temp_oauth_secret: str = url_parameters.get("oauth_token_secret")[0]
        return login_url, temp_oauth_token, temp_oauth_secret

    def get_permanent_credentials(self,
                                  temp_oauth_token: str,
                                  temp_oauth_secret: str,
                                  verifier: str
                                  ) -> EtsyOauthCredentials:
        temp_session = requests_oauthlib.OAuth1Session(self.api_key,
                                                       client_secret=self.shared_secret,
                                                       resource_owner_key=temp_oauth_token,
                                                       resource_owner_secret=temp_oauth_secret,
                                                       verifier=verifier
                                                       )
        permanent_token_request = temp_session.request(
            method="GET",
            url=f"{self.api_base_url}/oauth/access_token",
        )
        url_parameters: dict = urllib.parse.parse_qs(permanent_token_request.content.decode())

        # TODO: Separate resource owner credentials from client credentials.
        # Maybe require resource owner credentials as a kwarg for every Oauth required endpoint?
        return EtsyOauthCredentials(
            client_key=self.api_key,
            client_secret=self.shared_secret,
            resource_owner_key=url_parameters.get("oauth_token")[0],
            resource_owner_secret=url_parameters.get("oauth_token_secret")[0]
        )

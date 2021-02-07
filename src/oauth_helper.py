import requests_oauthlib
import typing


class OauthFlowFailed(Exception):
    def __init__(self, content):
        print("Oauth flow failed?")
        print(content)

class EtsyOauthHelper:
    def __init__(self, api_key: str, shared_secret: str, mode: str = "code"):
        self.api_key = api_key
        self.shared_secret = shared_secret
        self.session: requests_oauthlib.OAuth1Session = requests_oauthlib.OAuth1Session(api_key, client_secret=shared_secret)

    def get_login_url(self, permission_scopes: typing.List[str]):
        permission_scopes_str = " ".join(permission_scopes)
        response = self.session.request(
            method="GET",
            params={
                "scope": permission_scopes_str
            }
        )
        if response.status_code != 200:
            raise OauthFlowFailed(response.content)

        print(response.content)
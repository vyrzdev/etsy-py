# EtsyPy ~ The only working Etsy API wrapper!

This wrapper auto-generates itself from the API spec provided by Etsy at `openapi.etsy.com/v2/`

Instead of generating at runtime, it generates itself as the API changes through a set of Github Actions, this means you need to be sure to keep it up to date! You can check if you are up to date by calling `{{packagename}}.need_update()`

^^^ Planning to implement two update categories, with ones that effect large programmatic changes raising a separate exception to simple method table updates.

By pre-generating the API, this wrapper can take advantage of the `typing` module, and stub files to provide autocomplete. Hints for Etsy parameters are planned.



## Basic Usage:

```python
import {{packagename}}

# EtsyPy uses pluggable Requesters, that handle authentication, and pre-processing of requests. 
# When initializing the Requester, you must specify the authentication mode:
# oauth_1 | api_key 
# api_key authentication mode:

requester = {{packagename}}.rq.EtsyRequester(
	auth_mode="api_key",
    api_key="$token",
    api_base_url="https://openapi.etsy.com/v2" # <-- Without the trailing slash!
)

# Oauth 1 authentication mode: <-- Still being figured out, may change aggressively between updates!

oauth_credentials = {{packagename}}.rq.EtsyOauthCredentials(
	client_key="$api_key",
    client_secret="$shared_secret",
    resource_owner_key="$oauth_token",
    resource_owner_secret="$oauth_token_secret"
) # For help getting these credentials, scroll down to the Oauth Helper section.

```


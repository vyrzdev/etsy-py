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
    api_base_url="https://openapi.etsy.com/v2" # <-- Without the trailing slash! (is default)
)

# Oauth 1 authentication mode: <-- Still being figured out, may change aggressively between updates!

oauth_credentials = {{packagename}}.rq.EtsyOauthCredentials(
	client_key="$api_key",
    client_secret="$shared_secret",
    resource_owner_key="$oauth_token",
    resource_owner_secret="$oauth_token_secret"
) # For help getting these credentials, scroll down to the Oauth Helper section.

requester = {{packagename}}.rq.EtsyRequester(
	auth_mode="oauth_1",
    oauth_credentials=oauth_credentials
)

# Now we initialise a client.

etsy_client = {{packagename}}.client.EtsyClient(requester)

# With this client you can call any API method, e.g.

etsy_client.findAllFeaturedListings() # <-- You can find these names listed on the Etsy Documentation.

# URL arguments, like /listings/:listing_id, should be passed into their respective methods as positional arguments, in the order that they appear. They will be URL-Encoded automatically, but must be passed in as strings.
etsy_client.getListing("$listing_id")

# Query parameters should be passed into their respective methods as a dictionary, through the query_params keyword argument.
etsy_client.findAllFeaturedListings(query_params={
    "limit": 25,
    "offset": 2,
    "page": 6,    
})

# POST and PUT requests that contain JSON data should be passed into methods through the data kwarg. 

# ^^^ I expect problems to arise converting objects, if you find a problem please submit an issue.

etsy_client.updateListing("$listing_id", data={
    "title": "$product_title",
})

# If a request fails to complete for technical reasons, it will raise its expected exception from the requests library, however if Etsy returns a failed status code, the response object will return false on its .ok() method.
# Requests return an EtsyResponse object, with the standard requests.Response object contained within.


```


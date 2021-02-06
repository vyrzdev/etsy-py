# EtsyPy ~ Not yet on PyPi

### The only semi-decent Etsy API wrapper for Python!
(Built for v2 API.)

This wrapper will remain up-to-date, as it autogenerates itself from the API spec provided [here](https://openapi.etsy.com/v2/).
Don't worry though, it generates itself though GitHub Actions, no runtime generation here!

The wrapper also takes advantage of the `typing` module, as well as generating stub files to provide auto-completion. (Tested working in PyCharm)

---------------------------------------------------------------------------------------------------------------------------------------------

## Basic Usage

```python

from <insert_package_name> import client, rq

etsy_requester = rq.EtsyRequester(
  auth_mode="api_key", 
  api_key="____________"
) # Only api_key auth mode is supported thus far, Oauth on its way!

etsy_client = client.EtsyClient(etsy_requester)

etsy_client.getListing("1200020202") # Returns EtsyResponse object, with attr response, type: requests.Response

# Read further down for details on each object type.
```

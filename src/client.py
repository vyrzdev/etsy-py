import requests
from . import rq, methods
from inspect import getmembers, isfunction


class EtsyClient:
    def __init__(self, requester, api_base_url="https://openapi.etsy.com/v2", debug=False):
        self.api_base_url = api_base_url
        self.requester = requester
        self.debug = debug


method_function_objects = getmembers(methods, isfunction)

for method_name, method_object in method_function_objects:
    setattr(EtsyClient, method_name, method_object)
from . import rq
import typing

class EtsyClient:
    def __init__(self, requester: rq.EtsyRequester, api_base_url: str = ..., debug: bool = ...) -> EtsyClient:  ...

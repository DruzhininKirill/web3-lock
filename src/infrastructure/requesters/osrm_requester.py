import inject
from httpx import AsyncClient
from yarl import URL


class Requester:
    ROUTE_PATH = URL("route/v1/driving/")

    def __init__(self, base_url: str, http_client: AsyncClient) -> None:
        self._base_url = URL(base_url)
        self._http_client = http_client


@inject.autoparams()
def requester(requester: Requester):
    return requester

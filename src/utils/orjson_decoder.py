import httpx
import orjson


def response_to_json(response: httpx.Response):
    return orjson.loads(response.text)

import logging
from typing import Optional

import httpx
import inject
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from sqlalchemy.ext.asyncio import AsyncEngine

from infrastructure.repositories import Repository
from infrastructure.requesters.osrm_requester import Requester
from routers.tms_economy_calculations_router import router as tms_economy_calculations_router
from settings import Settings


app = FastAPI(default_response_class=ORJSONResponse)
app.include_router(tms_economy_calculations_router)
engine: Optional[AsyncEngine] = None
httpx_client: Optional[httpx.AsyncClient] = None
repo: Optional[Repository] = None


def config(binder):
    global engine, httpx_client, repo
    # engine = create_async_engine(Settings.PG_URL)
    repo = Repository(engine)
    binder.bind(Repository, repo)
    # backend_requester = BackendRequester(Settings.BACKEND_API_URL)
    # binder.bind(BackendRequester, backend_requester)
    httpx_client = httpx.AsyncClient(
        headers={"User-Agent": "tms-economy"},
        timeout=Settings.HTTP_TIMEOUT,
        limits=httpx.Limits(
            max_connections=Settings.MAX_CONNECTIONS,
            max_keepalive_connections=Settings.MAX_KEEPALIVE_CONNECTIONS,
            keepalive_expiry=Settings.KEEPALIVE_EXPIRY,
        ),
    )
    osrm_requester = Requester(Settings.WEB3_API_URL, httpx_client)
    binder.bind(Requester, osrm_requester)


@app.on_event("startup")
async def startup_event():
    inject.configure(config)


@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Shutting down...")

    await engine.dispose()
    await httpx_client.aclose()

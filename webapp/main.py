import gc

from fastapi import FastAPI
from SPARQLWrapper import SPARQLWrapper
from contextlib import asynccontextmanager
from starlette.middleware.cors import CORSMiddleware

from api import api_router as api_router_v1
from fastapi_globals import GlobalsMiddleware, g

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    sparql = SPARQLWrapper("http://89.40.142.15:7200/repositories/LARepo")
    g.set_default("sparql", sparql)

    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    print("startup fastapi")
    yield

    # shutdown
    g.cleanup()
    gc.collect()


app = FastAPI(
    title="Bitsei Los Angeles Ontology API",
    version="0.0.1",
    openapi_url="/api/v1/openapi.json",
    lifespan=lifespan,
)

app.add_middleware(GlobalsMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello Los Angeles :)"}


app.include_router(api_router_v1, prefix="/api/v1")

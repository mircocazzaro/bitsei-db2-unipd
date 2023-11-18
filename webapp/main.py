import gc

from fastapi import FastAPI
from SPARQLWrapper import SPARQLWrapper
from contextlib import asynccontextmanager
from starlette.middleware.cors import CORSMiddleware

from api import api_router as api_router_v1
from fastapi_globals import GlobalsMiddleware, g


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    sparql = SPARQLWrapper("http://89.40.142.15:7200/repositories/LARepo")
    g.set_default("sparql", sparql)
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


class CustomException(Exception):
    http_code: int
    code: str
    message: str

    def __init__(
            self,
            http_code: int = 500,
            code: str | None = None,
            message: str = "This is an error message",
    ):
        self.http_code = http_code
        self.code = code if code else str(self.http_code)
        self.message = message


@app.get("/")
async def root():
    return {"message": "Hello Los Angeles :)"}


app.include_router(api_router_v1, prefix="/api/v1")

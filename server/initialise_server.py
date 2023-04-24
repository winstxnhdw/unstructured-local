from asyncio import run

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from hypercorn.asyncio import serve

from server.api import v1
from server.config import Config


def initialise_server():
    """
    Summary
    -------
    initialize the server
    """
    app = FastAPI(root_path='/api')
    app.include_router(v1)
    app.on_event('startup')(lambda: print('The server has started!'))
    app.on_event('shutdown')(lambda: print('The server has shutdown!'))
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*'],
    )

    server = serve(app, Config()) # type: ignore
    run(server)

from fastapi import FastAPI, responses
from fastapi.openapi.utils import get_openapi
from expressly_server.routers.route import router

__version__ = "0.0.1"

app = FastAPI(
    title="Expressly AI Server",
    description="Expressly is your ultimate tool for transforming text effortlessly.",
    version=__version__,
    docs_url="/docs",
    redoc_url="/redoc",
)


app = FastAPI()


@app.get("/", include_in_schema=False)
async def root() -> responses.RedirectResponse:
    """
    Redirects the root URL to the API documentation page.

    Returns:
        RedirectResponse: A response object that redirects the client to the "/docs" URL.
    """

    return responses.RedirectResponse("/docs")

# Include routers
app.include_router(router, prefix="/app/v1", tags=["Operations"])


def _custom_openapi() -> dict:
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Expressly AI Server",
        description="Expressly is your ultimate tool for transforming text effortlessly.",
        version=__version__,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = _custom_openapi


def main() -> None:
    """
    The main entry point of the application.

    This function starts the FastAPI server using Uvicorn. It serves the API
    on the specified host and port. The function is intended to be run
    directly when the script is executed.

    Notes:
        - The 'nosec B104' comment is used to suppress a security warning
          related to binding to all network interfaces.
    """

    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10000)


if __name__ == "__main__":
    main()

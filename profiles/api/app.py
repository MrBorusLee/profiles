from fastapi import APIRouter, FastAPI, Request, status
from fastapi.exceptions import RequestValidationError, StarletteHTTPException
from fastapi.responses import JSONResponse

from profiles.settings import settings

from .errors import APIException, ErrorCode, ErrorResponse
from .routers.meta import meta_router
from .routers.profiles import profiles_router

app = FastAPI(title="profiles API")
api_router = APIRouter(prefix="/api")
api_router.include_router(meta_router, prefix="/meta")
api_router.include_router(profiles_router, prefix="/profiles")
app.include_router(api_router)


@app.exception_handler(APIException)
async def api_exception_handler(_: Request, exc: APIException):
    return JSONResponse(
        status_code=exc.status_code,
        headers=exc.headers,
        content=ErrorResponse(
            error_code=exc.error_code,
            message=exc.message,
            details=exc.detail,
        ).model_dump(),
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(_: Request, exc: StarletteHTTPException):
    """
    Map FastAPI exceptions to the API error format
    """
    error_code = ErrorCode.common_error

    return JSONResponse(
        status_code=exc.status_code,
        headers=exc.headers,
        content=ErrorResponse(
            error_code=error_code,
            message=exc.detail if isinstance(exc.detail, str) else "Unknown error",
            details=exc.detail,
        ).model_dump(),
    )


@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(_: Request, exc: RequestValidationError):
    message = "Request data is not valid"

    if exc.errors():
        message = "".join(error["msg"] for error in exc.errors())

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=ErrorResponse(
            error_code=ErrorCode.common_validation_error,
            message=message,
            details=exc.errors(),
        ).model_dump(),
    )


@app.exception_handler(Exception)
async def base_exception_handler(_: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ErrorResponse(
            error_code=ErrorCode.common_internal_error,
            message="Unknown error",
            details=f"{exc}" if settings.is_local_env() else None,
        ).model_dump(),
    )

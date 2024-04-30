from fastapi import APIRouter

from profiles.api.routers.profiles import create, get_one

profiles_router = APIRouter(tags=["profiles"])
profiles_router.include_router(create.router)
profiles_router.include_router(get_one.router)

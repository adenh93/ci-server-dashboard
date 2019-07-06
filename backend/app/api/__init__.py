from fastapi import APIRouter
from .endpoints.main import router as main_router
from .endpoints.auth import router as auth_router
from .endpoints.ci import router as build_router
from .endpoints.users import router as user_router

router = APIRouter()
router.include_router(main_router)
router.include_router(auth_router)
router.include_router(build_router)
router.include_router(user_router)

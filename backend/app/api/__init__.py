from fastapi import APIRouter
from .endpoints.system import router as system_router
from .endpoints.auth import router as auth_router
from .endpoints.ci import router as ci_router
from .endpoints.users import router as user_router

router = APIRouter()
router.include_router(system_router, prefix='/system')
router.include_router(auth_router, prefix='/auth')
router.include_router(ci_router, prefix='/ci')
router.include_router(user_router, prefix='/user')

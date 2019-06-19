from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/hello")
async def get_hello():
    return JSONResponse({'hello': 'world'})

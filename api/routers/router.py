from fastapi import APIRouter

router = APIRouter()

@router.get("/empty")
async def empty():
    return 'empty'
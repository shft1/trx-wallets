from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import WalletAddress
from app.core.db import get_async_session

router = APIRouter()


@router.post("/")
async def save_wallet(
    adress: WalletAddress, session: AsyncSession = Depends(get_async_session)
):
    pass

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.integrations import get_wallet_from_address
from app.api.schemas import WalletAddress
from app.core.db import get_async_session

router = APIRouter()


@router.post("/")
async def save_wallet(
    address: WalletAddress, session: AsyncSession = Depends(get_async_session)
):
    wallet_info = await get_wallet_from_address(address.address)
    return wallet_info

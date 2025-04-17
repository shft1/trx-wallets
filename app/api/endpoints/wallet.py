from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.integrations import get_wallet_from_address
from app.api.schemas import WalletAddressSchema, WalletInfoSchema
from app.core.db import get_async_session
from app.services import wallet_address_service, wallet_info_service

router = APIRouter()


@router.post("/")
async def saving_wallet_status(
    address: WalletAddressSchema,
    session: AsyncSession = Depends(get_async_session),
):
    info_dict = await get_wallet_from_address(address.address)
    info = WalletInfoSchema(**info_dict)

    wallet_address = await wallet_address_service.get_or_create(
        address, session
    )
    wallet_info = await wallet_info_service.create(
        obj=info, session=session, address_id=wallet_address.id
    )
    return wallet_info


@router.get("/")
async def receiving_wallets_with_status(
    session: AsyncSession = Depends(get_async_session),
):
    wallets_with_info = await wallet_address_service.get_multi(session)

    return wallets_with_info

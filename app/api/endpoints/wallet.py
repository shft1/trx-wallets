from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.integrations import get_wallet_from_address
from app.api.schemas import (
    WalletAddressCreateSchema,
    WalletAddressDBSchema,
    WalletInfoCreateSchema,
    WalletInfoDBSchema,
)
from app.core.db import get_async_session
from app.services import wallet_address_service, wallet_info_service

router = APIRouter()


@router.post("/")
async def saving_wallet_status(
    address: WalletAddressCreateSchema,
    session: AsyncSession = Depends(get_async_session),
) -> WalletInfoDBSchema:
    info_dict = await get_wallet_from_address(address.address)
    info = WalletInfoCreateSchema(**info_dict)

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
) -> Page[WalletAddressDBSchema]:
    wallets_with_info = await wallet_address_service.get_multi(session)
    return wallets_with_info

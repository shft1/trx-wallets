from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.api.schemas.wallet_address import WalletAddressCreateSchema
from app.models import WalletAddress
from app.services.base import BaseService


class WalletAddressService(BaseService):
    async def get_multi(self, session: AsyncSession):
        stmt = select(self.model).options(selectinload(self.model.wallet_info))
        return await paginate(session, stmt)

    async def get_or_create(
        self, address: WalletAddressCreateSchema, session: AsyncSession
    ):
        stmt = select(self.model).where(self.model.address == address.address)
        wallet_address = (await session.execute(stmt)).scalars().first()
        if wallet_address:
            return wallet_address
        wallet_address = await self.create(obj=address, session=session)
        return wallet_address


wallet_address_service = WalletAddressService(WalletAddress)

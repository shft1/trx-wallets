from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import WalletData
from app.models import WalletModel


class WalletService:
    model = WalletModel

    @classmethod
    async def create_wallet(cls, wallet: WalletData, session: AsyncSession):
        pass


wallet_service = WalletService()

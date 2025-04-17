from app.models import WalletInfo
from app.services.base import BaseService


class WalletInfoService(BaseService):
    pass


wallet_info_service = WalletInfoService(WalletInfo)

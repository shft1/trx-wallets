from tronpy import AsyncTron
from tronpy.providers import AsyncHTTPProvider

from app.core.config import config


async def get_wallet_from_address(address: str):
    http_tron_provider = AsyncHTTPProvider(api_key=config.api_key_tron)
    async with AsyncTron(
        provider=http_tron_provider, network="mainnet"
    ) as client:
        try:
            account = await client.get_account(address)
            return {
                "bandwidth": account.get("bandwidth", 0),
                "energy": account.get("energy", 0),
                "balance": account.get("balance") / 1_000_000,
            }
        except Exception as e:
            return {"error": str(e)}

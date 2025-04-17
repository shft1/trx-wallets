from fastapi import APIRouter

from app.api.endpoints import wallet_router

main_router = APIRouter()


main_router.include_router(wallet_router, prefix="/wallet", tags=["Wallet"])

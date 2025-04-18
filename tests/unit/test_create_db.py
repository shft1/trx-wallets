import pytest
from sqlalchemy import select

from app.api.schemas import WalletAddressCreateSchema, WalletInfoCreateSchema
from app.models import WalletAddress, WalletInfo
from app.services.base import BaseService
from tests.conftest import TestingSessionLocal


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "model, obj, data, address_id",
    [
        (
            WalletAddress,
            WalletAddressCreateSchema,
            {"address": "TPAjvJPPGTFg9kyWdRDNJ28XUbCSsTWmd5"},
            None,
        ),
        (
            WalletInfo,
            WalletInfoCreateSchema,
            {
                "bandwidth": 0,
                "energy": 0,
                "balance": 36897.740229,
            },
            1,
        ),
    ],
)
async def test_create_db(model, obj, data, address_id):
    async with TestingSessionLocal() as session:
        await BaseService(model).create(obj(**data), session, address_id)
        data = (await session.execute(select(model))).scalars().all()
        assert len(data) == 1

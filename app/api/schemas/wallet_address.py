from typing import Annotated

from pydantic import AfterValidator, BaseModel, ConfigDict

from app.api.schemas.wallet_info import WalletInfoDBSchema


def is_correct(value: str):
    if not value.startswith("T"):
        raise ValueError("Адрес кошелька должен начинаться с 'T'!")
    if len(value) != 34:
        raise ValueError("Неккоректный адрес кошелька!")
    return value


class WalletAddressCreateSchema(BaseModel):
    address: Annotated[str, AfterValidator(is_correct)]


class WalletAddressDBSchema(WalletAddressCreateSchema):
    model_config = ConfigDict(from_attributes=True)

    wallet_info: list[WalletInfoDBSchema]

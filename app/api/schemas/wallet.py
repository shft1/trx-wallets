from typing import Annotated

from pydantic import AfterValidator, BaseModel, ConfigDict


class WalletBase(BaseModel):
    bandwidth: int
    energy: int
    balance: float


class WalletDB(WalletBase):
    model_config = ConfigDict(from_attributes=True)


class WalletData(WalletBase):
    pass


def is_correct(value: str):
    if not value.startswith("T"):
        raise ValueError("Адрес кошелька должен начинаться с 'T'!")
    if len(value) != 34:
        raise ValueError("Неккоректный адрес кошелька!")
    return value


class WalletAddress(BaseModel):
    address: Annotated[str, AfterValidator(is_correct)]

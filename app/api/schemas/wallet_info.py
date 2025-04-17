from pydantic import BaseModel, ConfigDict


class WalletInfoBaseSchema(BaseModel):
    bandwidth: int
    energy: int
    balance: float


class WalletInfoCreateSchema(WalletInfoBaseSchema):
    pass


class WalletInfoDBSchema(WalletInfoBaseSchema):
    model_config = ConfigDict(from_attributes=True)

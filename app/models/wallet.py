from sqlalchemy import Column, Float, Integer

from app.core.db import Base


class WalletModel(Base):
    bandwidth = Column(Integer)
    energy = Column(Integer)
    balance = Column(Float)

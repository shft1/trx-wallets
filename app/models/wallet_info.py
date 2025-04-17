from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.core.db import Base


class WalletInfo(Base):
    bandwidth = Column(Integer, nullable=False)
    energy = Column(Integer, nullable=False)
    balance = Column(Float, nullable=False)
    datetime = Column(DateTime, default=datetime.now())
    address = Column(Integer, ForeignKey("walletaddress.id"))

    wallet_address = relationship(
        "WalletAddress", back_populates="wallet_info"
    )

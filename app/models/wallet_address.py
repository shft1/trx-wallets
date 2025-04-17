from sqlalchemy import CheckConstraint, Column, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class WalletAddress(Base):
    address = Column(String(34), nullable=False, unique=True)

    wallet_info = relationship("WalletInfo", back_populates="wallet_address")

    __table_args__ = (
        CheckConstraint("length(address) = 34", name="correct_address"),
    )

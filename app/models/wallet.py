from sqlalchemy import Column, Float, Integer

from app.core.db import Base


class Wallet(Base):
    bandwidth = Column(Integer)
    energy = Column(Integer)
    balance = Column(Float)

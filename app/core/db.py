from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr

from app.core.config import config


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)


engine = create_async_engine(config.database_url)

async_session = async_sessionmaker(engine)


async def get_async_session():
    async with async_session() as session:
        yield session

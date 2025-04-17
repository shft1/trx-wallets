from sqlalchemy.ext.asyncio import AsyncSession


class BaseService:
    def __init__(self, model):
        self.model = model

    async def create(self, obj, session: AsyncSession, address_id: int = None):
        obj_dict = obj.model_dump()
        if address_id:
            obj_dict["address"] = address_id
        obj_model = self.model(**obj_dict)
        session.add(obj_model)
        await session.commit()
        await session.refresh(obj_model)
        return obj_model

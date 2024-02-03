from typing import TypeVar, Generic, List, Type

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)


class GetAllCreateBase(Generic[ModelType, CreateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_all(
            self,
            session: AsyncSession
    ) -> List[ModelType]:
        db_objs = await session.scalars(select(self.model))
        return db_objs.all()

    async def create(
            self,
            new_obj_json: CreateSchemaType,
            session: AsyncSession,
    ) -> ModelType:
        new_obj_dict = new_obj_json.dict()
        new_obj_db = self.model(**new_obj_dict)
        session.add(new_obj_db)
        await session.commit()
        await session.refresh(new_obj_db)
        return new_obj_db

from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy import insert, update, delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.db.db import get_async_db
from src.shared.exceptions import DuplicateException
from src.shared.utils import filter_by_gen


class BaseMixin:
    def __init__(self, db: AsyncSession = Depends(get_async_db)):
        self.db = db

    async def execute(self, query, commit: bool = False):
        result = await self.db.execute(query)
        if commit:
            await self.db.commit()
        return result

    async def return_scalars_(self, query, is_unique: bool = False):
        result = await self.execute(query)
        if is_unique:
            return result.unique().scalars().all()
        return result.scalars().all()

    async def return_scalar_(self, query, is_unique: bool = False):
        result = await self.execute(query)
        if is_unique:
            return result.unique().scalar()
        return result.scalar()

    async def return_scalar_one_(self, query, is_unique: bool = False):
        result = await self.execute(query)
        if is_unique:
            return result.unique().scalar_one()
        return result.scalar_one()

    @property
    def model(self):
        raise NotImplementedError



class ReceiveMixin(BaseMixin):
    async def all(self, skip: int = 0, limit: int = 100, **filters):
        query = select(self.model).limit(limit).offset(skip).filter_by(**filters)
        return await self.return_scalars_(query)


class CreateMixin(BaseMixin):
    async def create(self, item: BaseModel):
        try:
            query = insert(self.model).returning(self.model).values(**item.dict())
            cursor = await self.execute(query, True)
            return cursor.fetchone()
        except IntegrityError:
            raise DuplicateException


class UpdateMixin(BaseMixin):
    async def _update_fields(self, instance, item: BaseModel):
        for var, value in item.dict().items():
            setattr(instance, var, value)
        return instance

    async def update(
            self,
            id: int = None,
            item: BaseModel = None,
            updated_fields: dict = None,
            **filters
    ):
        filter_by = filter_by_gen(id, **filters)
        query = update(self.model).returning(self.model).filter_by(**filter_by)

        if updated_fields:
            query = query.values(**updated_fields)

        if item:
            query = query.values(**item.dict())

        cursor = await self.execute(query, True)
        return cursor.fetchone()


class DeleteMixin(BaseMixin):
    async def delete(self, id: int = None, **filters):
        query = delete(self.model).filter_by(**filter_by_gen(id, **filters))
        await self.execute(query, True)


class CRUDRepository(ReceiveMixin, CreateMixin, UpdateMixin, DeleteMixin):
    pass

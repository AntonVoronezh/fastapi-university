from fastapi import Depends
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

import src.models as models
from src.db.config import get_settings
from src.models.decorators import check_exist
from src.shared.utils import filter_by_gen

engine = create_async_engine(
    get_settings().database_url, echo=True
)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_db():
    async with async_session() as session:
        try:  # noqa: WPS501
            yield session
        except Exception:
            await session.rollback()
        finally:
            await session.close()


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


class CRUDRepository(ReceiveMixin):
    pass


class StudentService(CRUDRepository):
    model = models.Student

    async def all(
            self,
            skip: int = 0,
            limit: int = 100,
            **filters,
    ):
        query = (
            select(self.model)

            .offset(skip)
            .limit(limit)
            .filter_by(**filters)
            .order_by(func.lower(self.model.first_name))
        )

        return await self.return_scalars_(query, True)

    @check_exist
    async def get(self, id: int = None, **filters):
        filter_by = filter_by_gen(id, **filters)

        query = select(self.model).filter_by(**filter_by)
        return await self.return_scalar_(query)

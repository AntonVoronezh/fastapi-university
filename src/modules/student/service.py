from sqlalchemy import func
from sqlalchemy.future import select

import src.models as models
from src.models.decorators import check_exist
from src.shared.mixins import CRUDRepository
from src.shared.utils import filter_by_gen




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

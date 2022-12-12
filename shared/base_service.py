from typing import TypeVar, Type, Optional, Generic, Any

from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.db import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], db_session: Session):
        self.model = model
        self.db_session = db_session

    def get(self, id: Any) -> Optional[ModelType]:
        obj: Optional[ModelType] = self.db_session.query(self.model).get(id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return obj

    def list(self) -> Optional[ModelType]:
        obj: list[ModelType] = self.db_session.query(self.model).all()
        if obj is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return obj

from fastapi import Depends
from sqlalchemy.orm import Session

from db.db import get_session
from models.housing import Housing
from modules.housing.dto import HousingCreateDTO, HousingUpdateDTO

from shared.base_service import BaseService


class HousingService(BaseService[Housing, HousingCreateDTO, HousingUpdateDTO]):
    def __init__(self, db_session: Session):
        super(HousingService, self).__init__(Housing, db_session)


def get_housing_service(db_session: Session = Depends(get_session)) -> HousingService:
    return HousingService(db_session)

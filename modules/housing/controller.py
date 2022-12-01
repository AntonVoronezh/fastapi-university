from http.client import HTTPException

from db.db import db
from modules.housing.dto import HousingDTO

from shared.controllers import api_router_factory
from tables.generate_tables import Housing

housing_router = api_router_factory("housing")


@housing_router.get('/', response_model=list[HousingDTO], status_code=200,
                     name='Получение всех корпусов')
def get_all_housing():
    faculties = db.query(Housing).all()
    return faculties


@housing_router.get('/{id}', response_model=HousingDTO, status_code=200, name='Получение корпуса')
def get_housing(id: int):
    housing = db.query(Housing).filter(Housing.id == id).first()

    return housing

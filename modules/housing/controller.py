from fastapi import Depends

from modules.housing.dto import HousingDTO
from modules.housing.service import HousingService, get_housing_service

from shared.controllers import api_router_factory

housing_router = api_router_factory("housing")


@housing_router.get('/', response_model=list[HousingDTO], status_code=200,
                    name='Получение всех корпусов')
def get_all_housing(housing_service: HousingService = Depends(get_housing_service)) -> list[HousingDTO]:
    return housing_service.list()


@housing_router.get('/{id}', response_model=HousingDTO, status_code=200, name='Получение корпуса')
def get_housing(id: int, housing_service: HousingService = Depends(get_housing_service)) -> HousingDTO:
    return housing_service.get(id)

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
#
#
# @housing_router.post('/', response_model=HousingWithFacultyDTO, status_code=201, name='Запись нового корпуса')
# def create_faculty(item: HousingBaseWithFacultyDto):
#     housing = db.query(Housing).filter(Housing.name == item.name).first()
#
#     if housing is not None:
#         return HTTPException(status_code=400, detail='Не существует')
#
#     new_housing = Housing(name=item.name)
#
#     db.add(new_housing)
#     db.commit()
#
#     return new_housing
#
#
# @housing_router.put('/{id}', response_model=HousingWithFacultyDTO, status_code=200, name='Обновление корпуса')
# def update_housing(id: int, item: HousingBaseWithFacultyDto):
#     housing_to_update = db.query(Housing).filter(Housing.id == id).first()
#
#     housing_to_update.name = item.name
#
#     db.commit()
#
#     return housing_to_update
#
#
# @housing_router.delete('/{id}', status_code=204, name='Удаление корпуса')
# def delete_housing(id: int):
#     housing_to_delete = db.query(Housing).filter(Housing.id == id).first()
#
#     if housing_to_delete is None:
#         raise HTTPException(status_code=404, detail='факультет не найден')
#
#     db.delete(housing_to_delete)
#     db.commit()
#
#     return housing_to_delete


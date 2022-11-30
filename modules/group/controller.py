from db.db import db
from modules.group.dto_plus_subjects import GroupPlusSubjectsDTO

from shared.controllers import api_router_factory
from tables.generate_tables import Group

group_router = api_router_factory("groups")


@group_router.get('/', response_model=list[GroupPlusSubjectsDTO], status_code=200,
                     name='Получение всех групп')
def get_all_groups():
    groups = db.query(Group).all()
    return groups


@group_router.get('/{id}', response_model=GroupPlusSubjectsDTO, status_code=200, name='Получение группы')
def get_group(id: int):
    group = db.query(Group).filter(Group.id == id).first()

    return group




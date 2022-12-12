from db.db import db
from fastapi import Depends
from modules.group.dto_plus_subjects import GroupPlusSubjectsDTO
from modules.group.service import GroupService, get_group_service
from shared.controllers import api_router_factory
from tables.generate_tables import Group

group_router = api_router_factory("groups")


@group_router.get('/', response_model=list[GroupPlusSubjectsDTO], status_code=200,
                  name='Получение всех групп')
def get_all_groups(group_service: GroupService = Depends(get_group_service)) -> list[GroupPlusSubjectsDTO]:
    return group_service.list()


@group_router.get("/{id}", response_model=GroupPlusSubjectsDTO, status_code=200,
                  name='Получение группы')
async def get_group(id:int, group_service: GroupService = Depends(get_group_service)) -> GroupPlusSubjectsDTO:
    return group_service.get(id)





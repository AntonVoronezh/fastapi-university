from fastapi import Depends
from sqlalchemy.orm import Session

from models.faculty import Faculty
from modules.group.dto import GroupUpdateDTO, GroupCreateDTO
from db.db import get_session
from models.group import Group

from shared.base_service import BaseService


class GroupService(BaseService[Group, GroupCreateDTO, GroupUpdateDTO]):
    def __init__(self, db_session: Session):
        super(GroupService, self).__init__(Group, db_session)


def get_group_service(db_session: Session = Depends(get_session)) -> GroupService:
    return GroupService(db_session)

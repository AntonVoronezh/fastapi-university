from pydantic import BaseModel

from modules.student.dto import StudentDTO


class GroupBaseDto(BaseModel):
    name: str
    course: int
    faculty_id: int | None
    housing_id: int | None


class GroupDTO(GroupBaseDto):
    id: int

    class Config:
        orm_mode = True


class GroupCreateDTO(GroupBaseDto):
    pass


class GroupUpdateDTO(GroupBaseDto):
    pass



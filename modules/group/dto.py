from pydantic import BaseModel


class GroupBaseDto(BaseModel):
    name: str
    course: int
    faculty_id: int or None
    housing_id: int or None


class GroupDTO(GroupBaseDto):
    id: int

    class Config:
        orm_mode = True



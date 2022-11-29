from pydantic import BaseModel


class GroupBaseDto(BaseModel):
    name: str
    course: int


class GroupDTO(GroupBaseDto):
    id: int

    class Config:
        orm_mode = True



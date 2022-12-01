from db.db import Base, engine

from models.faculty import Faculty
from models.group import Group
from models.housing import Housing
from models.subject import Subject
from models.group_subject import group_subject
from models.faculty_info import FacultyInfo
from models.student import Student
from models.student_info import StudentInfo


Base.metadata.create_all(bind=engine)

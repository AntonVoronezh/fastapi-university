from sqlalchemy import Column, Integer, ForeignKey, Table

from db.db import Base

group_subject = Table('group_subject', Base.metadata,
                      Column('group_id', Integer(), ForeignKey("group.id")),
                      Column('subject_id', Integer(), ForeignKey("subject.id"))
                      )

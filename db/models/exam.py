from sqlalchemy import Column, Integer
from db.base_class import Base


class Exam(Base):
    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    exam_number = Column(Integer, nullable=False)

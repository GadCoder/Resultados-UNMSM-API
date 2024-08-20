from sqlalchemy import Column, Integer, Float
from db.base_class import Base


class Score(Base):
    id = Column(Integer, primary_key=True)
    max_score = Column(Float, nullable=False)
    min_score = Column(Float, nullable=False)
    acceptance_rate = Column(Float, nullable=False)
    number_of_applicants = Column(Integer, nullable=False)

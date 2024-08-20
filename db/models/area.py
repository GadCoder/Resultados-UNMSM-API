from sqlalchemy import Column, Integer, String
from db.base_class import Base


class Area(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    initial_letter = Column(String(1), unique=True)

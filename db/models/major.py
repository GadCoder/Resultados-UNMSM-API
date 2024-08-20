from sqlalchemy import Column, Integer, String, ForeignKey
from db.base_class import Base


class Major(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    area_id = Column(Integer, ForeignKey("area.id"), nullable=False)

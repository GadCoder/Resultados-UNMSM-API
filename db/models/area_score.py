from sqlalchemy import Column, Integer, ForeignKey
from db.base_class import Base


class AreaScore(Base):
    id = Column(Integer, primary_key=True)

    area_id = Column(Integer, ForeignKey("area.id"))
    exam_id = Column(Integer, ForeignKey("exam.id"))
    score_id = Column(Integer, ForeignKey("score.id"))

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class OffensivePlay(Base):
    __tablename__ = "offensive_play"
    playType = Column(String, nullable=False)
    playId = Column(Integer, primary_key=True)

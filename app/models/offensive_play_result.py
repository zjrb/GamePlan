import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class offensive_play_result(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    pass_play_id = Column(UUID(as_uuid=True), ForeignKey("pass_play.id"), nullable=True)
    run_play_id = Column(UUID(as_uuid=True), ForeignKey("run_play.id"), nullable=True)
    caught = Column(Boolean, nullable=True)
    yards = Column(Integer, nullable=True)
    ball_carrier = Column(String, nullable=True)
    yac = Column(Integer, nullable=True)
    down = Column(Integer, nullable=False)
    distance = Column(Integer, nullable=False)
    touchdown = Column(Boolean, nullable=False)
    first_down = Column(Boolean, nullable=False)
    coverage = Column(String, nullable=True)
    blitz = Column(Boolean, nullable=True)
    defensive_personnel = Column(String, nullable=True)
    hash = Column(String, nullable=True)
    notes = Column(String, nullable=True)

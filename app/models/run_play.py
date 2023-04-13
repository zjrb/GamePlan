import uuid
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, UUID
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class run_play(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    formation_id = Column(
        UUID(as_uuid=True), ForeignKey("formation.id"), nullable=False
    )
    play_name = Column(String, nullable=False)
    offensive_play_results = relationship("offensive_play_result", backref="run_play")

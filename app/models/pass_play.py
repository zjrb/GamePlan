import uuid
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, UUID
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class pass_play(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    formation_id = Column(
        UUID(as_uuid=True), ForeignKey("formation.id"), nullable=False
    )
    play_name = Column(String, nullable=False)
    formation = relationship("formation", back_populates="pass_play")

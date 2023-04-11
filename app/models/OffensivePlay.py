import uuid

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class offensive_play(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    play_type = Column(String, nullable=False)
    pass_play_id = Column(UUID(as_uuid=True), ForeignKey("pass_play.id"))
    pass_play = relationship(
        "pass_play", foreign_keys=pass_play_id, back_populates="offensive_play"
    )

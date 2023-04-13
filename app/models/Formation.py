import uuid
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, UUID
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from .pass_play import pass_play


class formation(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    formation_name = Column(String, nullable=False)
    pass_play = relationship("pass_play", back_populates="formation")
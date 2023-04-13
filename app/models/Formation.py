import uuid
import uuid
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, UUID
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from .pass_play import pass_play
#changes

class formation(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    formation_name = Column(String, nullable=False)
    pass_plays = relationship("pass_play", backref="formation")
    run_plays = relationship("run_play", backref="formation")

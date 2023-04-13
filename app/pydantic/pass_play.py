from uuid import UUID
from typing import List, Optional
from pydantic import BaseModel


class pass_play(BaseModel):
    formation_id: UUID
    play_name: str

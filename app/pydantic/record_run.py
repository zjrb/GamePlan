from uuid import UUID
from typing import List, Optional
from pydantic import BaseModel


class record_run(BaseModel):
    play_name: str
    yards: int
    ball_carrier: str
    down: int
    distance: int
    touchdown: bool
    first_down: bool
    hash: str

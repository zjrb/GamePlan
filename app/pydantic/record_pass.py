from uuid import UUID
from typing import List, Optional
from pydantic import BaseModel


class record_pass(BaseModel):
    play_name: str
    caught: int
    yards: int
    ball_carrier: str
    yac: int
    down: int
    distance: int
    touchdown: bool
    first_down: int
    coverage: str
    blitz: bool
    hash: str

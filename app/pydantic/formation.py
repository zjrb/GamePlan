from uuid import UUID
from typing import List, Optional
from pydantic import BaseModel


class formation(BaseModel):
    formation_name: str

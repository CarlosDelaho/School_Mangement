from pydantic import BaseModel
from typing import Optional

class Roles(BaseModel):
    id: int=None
    name: str
    state: Optional[bool] = None
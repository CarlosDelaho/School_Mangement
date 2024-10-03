from pydantic import BaseModel
from typing import Optional

class Modules(BaseModel):
    id: int=None
    name: str
    description: Optional[str] = None
    state: Optional[bool] = None
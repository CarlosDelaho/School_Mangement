from pydantic import BaseModel
from typing import Optional

class Parameters(BaseModel):
    id: int = None
    reference: str
    name: str
    description: Optional[str] = None
    state: Optional[bool] = None

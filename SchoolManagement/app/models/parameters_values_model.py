from pydantic import BaseModel
from typing import Optional

class ParametersValues(BaseModel):
    id: int = None
    referene: str
    name: str
    description: Optional[str] = None
    parameter_id: int
    state: Optional[bool] = None

from pydantic import BaseModel
from typing import Optional

class Schools(BaseModel):
    id: int=None
    name: str
    address: Optional[str] = None
    phone: Optional[str] = None
    email: str
    type_school_id: int
    photo: Optional[str] = None
    website: Optional[str] = None
    state: Optional[bool] = None
    # created_at: str=None
    
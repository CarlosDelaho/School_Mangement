from pydantic import BaseModel
from typing import Optional

class Users(BaseModel):
    id: int = None
    role_id: int
    name: str
    last_name: str
    email: str
    phone: str
    document_type_id: int
    document_number: str
    password: str
    photo: Optional[str] = None
    state: Optional[bool] = None

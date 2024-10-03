from pydantic import BaseModel
from typing import Optional

class Permissions(BaseModel):
    id: int=None
    role_id: int
    module_id: int
    can_view: Optional[bool] = None
    can_edit: Optional[bool] = None
    can_delete: Optional[bool] = None

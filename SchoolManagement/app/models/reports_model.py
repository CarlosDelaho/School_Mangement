from pydantic import BaseModel
from typing import Optional

class Reports(BaseModel):
    id: int=None
    type_report_id: int
    reporter_id: int
    reported_user_id: int
    description: str
    state: Optional[bool] = None
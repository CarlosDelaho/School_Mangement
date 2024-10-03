from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Activities(BaseModel):
    id: int=None
    title: str
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    type_activity_id:int
    school_id:int
    state: Optional[bool] = None

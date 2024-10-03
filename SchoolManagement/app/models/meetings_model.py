from pydantic import BaseModel
from datetime import datetime, time
from typing import Optional

class Meetings(BaseModel):
    id: int=None
    title: str
    description: Optional[str] = None
    date: datetime
    time: time
    type_meeting_id: int
    school_id: int
    state: Optional[bool] = None

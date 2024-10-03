from pydantic import BaseModel
from typing import List

class ParticipantsActivities(BaseModel):
    id: int=None
    activity_id: int
    responsibles_ids: List[int]
    participants_ids:  List[int]
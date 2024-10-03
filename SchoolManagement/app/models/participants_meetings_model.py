from pydantic import BaseModel
from typing import List

class ParticipantsMeetings(BaseModel):
    id: int=None
    meeting_id: int
    responsibles_ids: List[int]
    participants_ids:  List[int]
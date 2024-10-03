from pydantic import BaseModel
class EvidenceActivities(BaseModel):
    id: int=None
    activity_id: int
    file: str
    uploaded_by: int
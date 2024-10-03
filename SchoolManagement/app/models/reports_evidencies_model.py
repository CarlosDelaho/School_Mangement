from pydantic import BaseModel

class ReportsEvidencies(BaseModel):
    id: int=None
    file: str
    uploaded_by: int
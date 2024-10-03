from pydantic import BaseModel

class SchoolsUsers(BaseModel):
    id: int = None
    user_id: int
    school_id: int


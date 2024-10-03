from pydantic import BaseModel
class CommentsActivities(BaseModel):
    id: int=None
    activity_id: int
    user_id: int
    comment: str
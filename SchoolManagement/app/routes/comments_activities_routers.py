from fastapi import APIRouter, HTTPException
from controllers.comments_activities_controller import *
from models.comments_activities_model import CommentsActivities

router = APIRouter()

nuevo_usuario = CommentsActivitiesController()


@router.post("/create_comments_activities")
async def create_comments_activities(comments_activities:CommentsActivities):
    rpta = nuevo_usuario.create_comments_activities(comments_activities)
    return rpta

@router.get("/get_comments_activities/{id}")
async def get_comments_activities(id: int):
    rpta = nuevo_usuario.get_comments_activities(id)
    return rpta

@router.get("/get_comments_activities")
async def get_comments_activities():
    rpta = nuevo_usuario.get_comments_activities()
    return rpta

@router.put("/edit_comments_activities/{id}")
async def edit_comments_activities(id:int, comments_activities:CommentsActivities):
    rpta = nuevo_usuario.edit_comments_activities(id,comments_activities)
    return rpta

@router.delete("/delete_comments_activities/{comments_activities_id}")
async def delete_comments_activities(comments_activities_id: int):
    rpta = nuevo_usuario.delete_comments_activities(comments_activities_id)
    return rpta
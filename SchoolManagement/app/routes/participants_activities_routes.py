from fastapi import APIRouter, HTTPException
from controllers.participants_activities_controller import *
from models.participants_activities_model import ParticipantsActivities
router = APIRouter()

new = ParticipantsActivitiesController()


@router.post("/create_participant_activity")
async def create_participant_activity(participant: ParticipantsActivities):
    rpta = new.create_participant_activity(participant)
    return rpta


@router.get("/get_participant_activity/{id}",response_model= ParticipantsActivities)
async def get_participant_activity(id: int):
    rpta = new.get_participant_activity(id)
    return rpta

@router.get("/get_participants_activities/")
async def get_participants_activities():
    rpta = new.get_participants_activities()
    return rpta

@router.put("/edit_participant_activity/{id}")
async def edit_participant_activity(id:int, participant:ParticipantsActivities):
    rpta = new.edit_participant_activity(id,participant)
    return rpta

@router.delete("/delete_participant_activity/{id}")
async def delete_participant_activity(id: int):
    rpta = new.delete_participant_activity(id)
    return rpta
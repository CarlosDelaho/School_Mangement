from fastapi import APIRouter, HTTPException
from controllers.participants_meetings_controller import *
from models.participants_meetings_model import ParticipantsMeetings

router = APIRouter()

new = ParticipantsMeetingsController()


@router.post("/create_participant_meeting")
async def create_participant_meeting(participant: ParticipantsMeetings):
    rpta = new.create_participant_meeting(participant)
    return rpta


@router.get("/get_participant_meeting/{id}")
async def get_participant_meeting(id: int):
    rpta = new.get_participant_meeting(id)
    return rpta

@router.get("/get_participants_meetings/")
async def get_participants_meetings():
    rpta = new.get_participants_meetings()
    return rpta

@router.put("/edit_participant_meeting/{id}")
async def edit_participant_meeting(id:int, participant:ParticipantsMeetings):
    rpta = new.edit_participant_meeting(id,participant)
    return rpta

@router.delete("/delete_participant_meeting/{id}")
async def delete_participant_meeting(id: int):
    rpta = new.delete_participant_meeting(id)
    return rpta
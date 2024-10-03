from fastapi import APIRouter, HTTPException
from controllers.activities_controller import *
from models.activities_model import Activities

router = APIRouter()

controller = ActivitiesController()


@router.post("/create_activity")
async def create_activity(activity: Activities):
    rpta = controller.create_activity(activity)
    return rpta

@router.get("/get_activity/{id}")
async def get_activity(id: int):
    rpta = controller.get_activity(id)
    return rpta

@router.get("/get_activities")
async def get_activities():
    rpta = controller.get_activities()
    return rpta

@router.put("/edit_activity/{id}")
async def edit_activity(id:int, activity: Activities):
    rpta = controller.edit_activity(id, activity)
    return rpta

@router.delete("/delete_activity/{id}")
async def delete_activity(id: int):
    rpta =controller.delete_activity(id)
    return rpta

@router.get("/get_parameter_values/{parameter_id}")
def get_parameter_values(parameter_id: int):
    return controller.get_parameter_values(parameter_id)
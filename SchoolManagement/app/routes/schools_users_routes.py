from fastapi import APIRouter, HTTPException
from controllers.schools_users_controller import *
from models.schools_users_model import SchoolsUsers

router = APIRouter()

new = SchoolsUsersController()


@router.post("/create_school_user")
async def create_school_user(SchoolUser:SchoolsUsers):
    rpta = new.create_school_user(SchoolUser)
    return rpta

@router.get("/get_school_user/{school_user_id}")
async def get_school_user(school_user_id: int):
    rpta = new.get_school_user(school_user_id)
    return rpta

@router.get("/get_schools_users/")
async def get_schools_users():
    rpta = new.get_schools_users()
    return rpta

@router.put("/edit_school_user/{school_user_id}")
async def edit_school_user(school_user_id:int, schoolUser:SchoolsUsers):
    rpta = new.edit_school_user(school_user_id,schoolUser)
    return rpta

@router.delete("/delete_school_user/{school_user_id}")
async def delete_school_user(school_user_id: int):
    rpta = new.delete_school_user(school_user_id)
    return rpta
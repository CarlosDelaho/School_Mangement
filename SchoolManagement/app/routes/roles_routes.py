from fastapi import APIRouter, HTTPException
from controllers.roles_controller import *
from models.roles_model import Roles

router = APIRouter()

controller = RolesController()


@router.post("/create_rol")
async def create_rol(roles: Roles):
    rpta = controller.create_rol(roles)
    return rpta

@router.get("/get_rol/{id}")
async def get_rol(id: int):
    rpta = controller.get_rol(id)
    return rpta

@router.get("/get_roles")
async def get_roles():
    rpta = controller.get_roles()
    return rpta

@router.put("/edit_rol/{id}")
async def edit_rol(id:int, roles: Roles):
    rpta = controller.edit_rol(id, roles)
    return rpta

@router.put("/delete_rol/{id}")
async def delete_rol(id: int):
    rpta = controller.delete_rol(id)
    return rpta
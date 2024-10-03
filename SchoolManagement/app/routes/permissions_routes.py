from fastapi import APIRouter, HTTPException
from controllers.permissions_controller import *
from models.permissions_model import Permissions

router = APIRouter()

controller = PermissionsController()


@router.post("/create_permission")
async def create_permission(permission:Permissions):
    rpta = controller.create_permission(permission)
    return rpta

@router.get("/get/permission/{id}")
async def get_permission(id: int):
    rpta = controller.get_permission(id)
    return rpta

@router.get("/get_permissions")
async def get_permissions():
    rpta = controller.get_permissions()
    return rpta

@router.put("/edit_permission/{id}")
async def edit_permission(id:int, permission: Permissions):
    rpta = controller.edit_permission(id, permission)
    return rpta

@router.delete("/delete_permission/{id}")
async def delete_permission(id: int):
    rpta = controller.delete_permission(id)
    return rpta
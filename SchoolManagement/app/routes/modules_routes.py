from fastapi import APIRouter, HTTPException
from controllers.modules_controller import *
from models.modules_model import Modules

router = APIRouter()

controller = ModulesController()


@router.post("/create_module")
async def create_module(module:Modules):
    rpta = controller.create_module(module)
    return rpta

@router.get("/get/module/{id}")
async def get_module(id: int):
    rpta = controller.get_module(id)
    return rpta

@router.get("/get_modules")
async def get_modules():
    rpta = controller.get_modules()
    return rpta

@router.put("/edit_module/{id}")
async def edit_module(id:int, module:Modules):
    rpta = controller.edit_module(id,module)
    return rpta

@router.delete("/delete_module/{id}")
async def delete_module(id: int):
    rpta = controller.delete_module(id)
    return rpta
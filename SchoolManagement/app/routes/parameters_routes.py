from fastapi import APIRouter, HTTPException
from controllers.parameters_controller import *
from models.parameters_model import Parameters

router = APIRouter()

nuevo_parametro = ParametersController()


@router.post("/create_parameter")
async def create_parameter(parameter: Parameters):
    rpta = nuevo_parametro.create_parameter(parameter)
    return rpta


@router.get("/get_parameter/{parameter_id}")
async def get_parameter(parameter_id: int):
    rpta = nuevo_parametro.get_parameter(parameter_id)
    return rpta

@router.get("/get_parameters/")
async def get_parameters():
    rpta = nuevo_parametro.get_parameters()
    return rpta

@router.put("/edit_parameter/{id}")
async def edit_parameter(id:int, parameter:Parameters):
    rpta = nuevo_parametro.edit_parameter(id,parameter)
    return rpta

@router.delete("/delete_parameter/{parameter_id}")
async def delete_parameter(parameter_id: int):
    rpta = nuevo_parametro.delete_parameter(parameter_id)
    return rpta
from fastapi import APIRouter, HTTPException
from controllers.parameters_values_controller import *
from models.parameters_values_model import ParametersValues

router = APIRouter()

nuevo_parametro = ParametersValuesController()


@router.post("/create_parameter_value")
async def create_parameter_value(parameter_value: ParametersValues):
    rpta = nuevo_parametro.create_parameter_value(parameter_value)
    return rpta


@router.get("/get_parameter_value/{parameter_value_id}")
async def get_parameter_value(parameter_value_id: int):
    rpta = nuevo_parametro.get_parameter_value(parameter_value_id)
    return rpta

@router.get("/get_parameters_values/")
async def get_parameters_values():
    rpta = nuevo_parametro.get_parameters_values()
    return rpta
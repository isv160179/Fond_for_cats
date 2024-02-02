from fastapi import APIRouter, Body

from app.crud.charity_project import create_charity_project
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectCreate

router = APIRouter()


@router.post('/charity_project/')
async def create_new_charity_project(
        new_project_json: CharityProjectCreate = Body(
            ...,
            examples=CharityProjectCreate.Config.schema_extra['examples']
        )
) -> CharityProject:
    new_project_db = await create_charity_project(new_project_json)
    return new_project_db

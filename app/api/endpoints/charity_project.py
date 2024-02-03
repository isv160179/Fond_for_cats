from fastapi import APIRouter, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_project_exist, check_name_duplicate
from app.core.db import get_async_session
from app.crud.charity_project import project_crud
from app.models.charity_project import CharityProject
from app.schemas.charity_project import (
    CharityProjectCreate,
    CharityProjectDB,
    CharityProjectUpdate,
)

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
)
async def create_charity_project(
        new_project_json: CharityProjectCreate = Body(
            ...,
            examples=CharityProjectCreate.Config.schema_extra['examples']
        ),
        session: AsyncSession = Depends(get_async_session),
) -> CharityProject:
    await check_name_duplicate(new_project_json.name, session)
    new_project_db = await project_crud.create(new_project_json, session)
    return new_project_db


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session),
):
    return await project_crud.get_all(session)


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
)
async def update_charity_project(
        project_id: int,
        project_json: CharityProjectUpdate = Body(
            ...,
            examples=CharityProjectUpdate.Config.schema_extra['examples']
        ),
        session: AsyncSession = Depends(get_async_session),
):
    project_db = await check_project_exist(project_id, session)
    if project_json.name is not None:
        await check_name_duplicate(project_json.name, session)
    return await project_crud.update(project_db, project_json, session)


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
)
async def delete_charity_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    project_db = await check_project_exist(project_id, session)
    project_db = await project_crud.delete(project_db, session)
    return project_db
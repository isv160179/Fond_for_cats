from fastapi import APIRouter, Body, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.charity_project import (
    create_charity_project,
    check_unique_name,
    read_all_project_from_db, get_project_by_id, update_charity_project,
    delete_charity_project
)
from app.models.charity_project import CharityProject
from app.schemas.charity_project import (
    CharityProjectCreate,
    CharityProjectDB,
    CharityProjectUpdate,
)

router = APIRouter(
    prefix='/charity_project',
    tags=['charity_projects']
)


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
)
async def create_new_charity_project(
        new_project_json: CharityProjectCreate = Body(
            ...,
            examples=CharityProjectCreate.Config.schema_extra['examples']
        ),
        session: AsyncSession = Depends(get_async_session),
) -> CharityProject:
    await check_name_duplicate(new_project_json.name, session)
    new_project_db = await create_charity_project(new_project_json, session)
    return new_project_db


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_meeting_rooms(
        session: AsyncSession = Depends(get_async_session),
):
    return await read_all_project_from_db(session)


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
)
async def partially_update_charity_project(
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
    return await update_charity_project(project_db, project_json, session)


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
)
async def remove_charity_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    project_db = await check_project_exist(project_id, session)
    project_db = await delete_charity_project(project_db, session)
    return project_db


async def check_project_exist(
        project_id: int,
        session: AsyncSession
) -> CharityProject:
    project_db = await get_project_by_id(project_id, session)
    if project_db is None:
        raise HTTPException(
            status_code=404,
            detail='Проект не найден!'
        )
    return project_db


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    if await check_unique_name(project_name, session):
        raise HTTPException(
            status_code=422,
            detail='Благотворительный проект с таким именем уже существует!',
        )

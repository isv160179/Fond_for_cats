from typing import Union, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import Boolean, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.charity_project import CharityProject
from app.schemas.charity_project import (
    CharityProjectCreate,
    CharityProjectUpdate,
)


async def create_charity_project(
        new_project_json: CharityProjectCreate,
        session: AsyncSession,
) -> CharityProject:
    new_project_dict = new_project_json.dict()
    new_project_db = CharityProject(**new_project_dict)
    session.add(new_project_db)
    await session.commit()
    await session.refresh(new_project_db)
    return new_project_db


async def read_all_project_from_db(
        session: AsyncSession,
) -> list[CharityProject]:
    projects_db = await session.execute(select(CharityProject))
    return projects_db.scalars().all()


async def update_charity_project(
        project_db: CharityProject,
        project_json: CharityProjectUpdate,
        session: AsyncSession,
) -> CharityProject:
    project_from_db_dict = jsonable_encoder(project_db)
    project_from_json_dict = project_json.dict(exclude_unset=True)
    for field in project_from_db_dict:
        if field in project_from_json_dict:
            setattr(project_db, field, project_from_json_dict[field])
    session.add(project_db)
    await session.commit()
    await session.refresh(project_db)
    return project_db


async def delete_charity_project(
        project_db: CharityProject,
        session: AsyncSession,
) -> CharityProject:
    await session.delete(project_db)
    await session.commit()
    return project_db


async def check_unique_name(
        field_name: str,
        session: AsyncSession,
) -> Union[None, Boolean]:
    exists_criteria = (
        select(CharityProject).where(
            CharityProject.name == field_name
        ).exists()
    )
    db_field_exists = await session.scalars(
        select(True).where(exists_criteria)
    )
    return db_field_exists.first()


async def get_project_by_id(
        project_id: int,
        session: AsyncSession,
) -> Optional[CharityProject]:
    return await session.get(CharityProject, project_id)

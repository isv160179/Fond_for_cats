from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.constants import (
    WARNING_PROJECT_NOT_FOUND,
    WARNING_PROJECT_NAME_NOT_UNIQUE
)
from app.crud.charity_project import project_crud
from app.models import CharityProject


async def check_project_exist(
        project_id: int,
        session: AsyncSession
) -> CharityProject:
    project_db = await project_crud.get_project_by_id(project_id, session)
    if project_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=WARNING_PROJECT_NOT_FOUND
        )
    return project_db


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    if await project_crud.check_unique_name(project_name, session):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=WARNING_PROJECT_NAME_NOT_UNIQUE,
        )

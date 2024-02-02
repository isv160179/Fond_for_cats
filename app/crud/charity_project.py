from app.core.db import AsyncSessionLocal
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectCreate


async def create_charity_project(
        new_project_json: CharityProjectCreate
) -> CharityProject:
    new_project_dict = new_project_json.dict()
    new_project_db = CharityProject(**new_project_dict)
    async with AsyncSessionLocal() as session:
        session.add(new_project_db)
        await session.commit()
        await session.refresh(new_project_db)
    return new_project_db

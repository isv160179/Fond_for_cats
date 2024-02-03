from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.donation import donation_crud
from app.models import Donation, User
from app.schemas.donation import DonationDB, DonationCreate, DonationShortDB

router = APIRouter()


@router.get(
    '/',
    response_model=list[DonationDB],
    response_model_exclude_none=True,
)
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session),
):
    return await donation_crud.get_all(session)


@router.post(
    '/',
    response_model=DonationShortDB,
    response_model_exclude_none=True,
)
async def create_donation(
        new_donation_json: DonationCreate = Body(
            ...,
            examples=DonationCreate.Config.schema_extra['examples']
        ),
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
) -> Donation:
    new_donation_db = await donation_crud.create(
        new_donation_json,
        session,
        user
    )
    return new_donation_db

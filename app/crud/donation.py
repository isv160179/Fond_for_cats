from app.crud.base import GetAllCreateBase
from app.models import Donation
from app.schemas.donation import DonationCreate


class CRUDDonation(
    GetAllCreateBase[Donation, DonationCreate]
):
    @staticmethod
    async def get_user_donations():
        pass


donation_crud = CRUDDonation(Donation)

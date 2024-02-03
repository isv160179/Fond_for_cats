from sqlalchemy import Column, Text

from app.models.base import Invest


class Donation(Invest):
    # user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

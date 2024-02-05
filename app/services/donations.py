from datetime import datetime
from typing import Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.base import InvestModel


async def investment(
        obj_for_invest: InvestModel,
        model: Type[InvestModel],
        session: AsyncSession
) -> InvestModel:
    objects = await session.scalars(
        select(model).where(model.fully_invested == 0).order_by(
            model.create_date)
    )
    for obj_from_invest in objects.all():
        money_for_append = min(
            obj_for_invest.full_amount - obj_for_invest.invested_amount,
            obj_from_invest.full_amount - obj_from_invest.invested_amount
        )
        obj_from_invest.invested_amount += money_for_append
        obj_for_invest.invested_amount += money_for_append

        for obj in [obj_from_invest, obj_for_invest]:
            if obj.full_amount == obj.invested_amount:
                obj.fully_invested = True
                obj.close_date = datetime.now()
                session.add(obj)
    await session.commit()
    await session.refresh(obj_for_invest)
    return obj_for_invest

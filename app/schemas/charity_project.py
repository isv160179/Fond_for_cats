from typing import Optional

from pydantic import BaseModel, Field, PositiveInt

from app.core.constants import PROJECT_CREATE_EXAMPLES


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None)
    full_amount: Optional[PositiveInt]


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., max_length=100)
    description: str = Field(..., )
    full_amount: PositiveInt = Field(..., )

    class Config:
        schema_extra = {
            'examples': PROJECT_CREATE_EXAMPLES
        }

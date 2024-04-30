from datetime import datetime
from enum import StrEnum

from fastapi import APIRouter
from pydantic import BaseModel

from profiles.api.deps import DBSession

router = APIRouter()


class Gender(StrEnum):
    male: str = "male"
    female: str = "female"


class CreateProfileDTO(BaseModel):
    """
    Имя
    Фамилия
    Дата рождения
    Пол
    Интересы
    Город
    Страницы с анкетой.
    """

    first_name: str
    last_name: str
    dob: datetime
    gender: Gender
    # TODO: add remaining fields


@router.post("/")
async def create_profile(db: DBSession, profile_dto: CreateProfileDTO):
    result = await db.execute(
        f"insert into profiles (first_name, last_name, dob) VALUES "
        f"('{profile_dto.first_name}', '{profile_dto.last_name}', '{profile_dto.dob}')"
    )
    return result

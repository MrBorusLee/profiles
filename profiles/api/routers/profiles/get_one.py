from fastapi import APIRouter

from profiles.api.deps import DBSession

router = APIRouter()


@router.get("/<profile_id>")
async def create_profile(db: DBSession, profile_id: str):
    result = await db.fetchrow(f"SELECT * FROM profiles where id='{profile_id}'")
    return result

from fastapi import APIRouter, Depends

from app.models.user import User
from app.schemas.user import UserOut
from app.utils.security import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserOut)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user

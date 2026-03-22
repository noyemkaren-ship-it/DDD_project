from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database.db import get_db
from database.repository.Bissnes_logic_repository import BusinessLogicRepository
from database.repository.user_repository import UserRepository
from schemas.returns.ret import Message
from schemas.user.user import UserSchema
from schemas.user.userlogin import UserShemaLogin

router = APIRouter()


@router.post("/withdraw")
async def withdraw(
        amount: int,
        username: str,
        db: Session = Depends(get_db)
):
    user_repo = UserRepository(db)
    user = user_repo.get_user_by_username(username)

    if not user:
        return Message(name="Withdraw", text="User not found", success=False)

    biz_repo = BusinessLogicRepository(db)
    result = biz_repo.withdraw(amount, user)
    return result


@router.post("/register")
async def register(
        user_data: UserSchema,
        db: Session = Depends(get_db)
):
    repo = UserRepository(db)
    result = repo.create_user(
        name=user_data.username,
        email=user_data.email,
        password=user_data.password
    )

    if not result.success:
        return result

    response = RedirectResponse(url=f"/profile/{user_data.username}", status_code=303)
    response.set_cookie("username", user_data.username, max_age=86400)
    return response


@router.post("/login")
async def login(
        user_data: UserShemaLogin,
        db: Session = Depends(get_db)
):
    repo = UserRepository(db)
    user = repo.get_user_by_email(user_data.email)

    if user and user.password == user_data.password:
        response = RedirectResponse(url=f"/profile/{user.username}", status_code=303)
        response.set_cookie("username", user.username, max_age=86400)
        return response

    return Message(
        name="Login",
        text="Invalid credentials",
        success=False
    )
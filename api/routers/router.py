from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from database.repository.user_repository import UserRepository
from schemas.returns.ret import Message
from schemas.user.create_user import CreateUserSchema
from schemas.user.userlogin import UserShemaLogin
from schemas.user.userret import UserReturnSchema

router = APIRouter()

@router.post("/deposit", tags=["Внести"])
async def deposit(amount: int, username: str):
    repo = UserRepository()
    result = repo.deposit(amount, username)
    return result

@router.post("/withdraw", tags=["Вывести"])
async def withdraw(amount: int, username: str):
    repo = UserRepository()
    result = repo.withdraw(amount, username)
    return result

@router.post("/register", tags=["Регистрация"])
async def register(user_data: CreateUserSchema):
    repo = UserRepository()
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


@router.post("/login", tags=["Вход"])
async def login(user_data: UserShemaLogin):
    repo = UserRepository()
    user = repo.get_user_by_email(user_data.email)

    if user and user.password == user_data.password:
        return {"message": "Login successful", "username": user.name}

    return Message(
        name="Login",
        text="Invalid credentials",
        success=False
    ), UserReturnSchema(
        username=user_data.username,
        password=user_data.password
    )

@router.get("/users", tags=["Все пользователи"])
async def get_all_users():
    repo = UserRepository()
    users = repo.get_user_all()
    return users


@router.get("/api/users/{username}/balance", tags=["API"])
async def get_balance(username: str):
    repo = UserRepository()
    user = repo.get_user_by_name(username)
    if not user:
        return {"error": "User not found"}
    return {"balance": user.balance}
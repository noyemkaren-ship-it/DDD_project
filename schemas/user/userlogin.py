from pydantic import BaseModel


class UserShemaLogin(BaseModel):
    password: str
    email: str
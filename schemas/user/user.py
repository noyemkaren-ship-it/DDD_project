
from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    userpassword: str
    useremail: EmailStr



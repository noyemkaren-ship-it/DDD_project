
from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    userpassword: str
    useremail: str
    userbalance: float



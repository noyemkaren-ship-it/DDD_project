from pydantic import BaseModel


class UserReturnSchema(BaseModel):
    username: str
    password: str
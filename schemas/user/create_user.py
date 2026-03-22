from pydantic import BaseModel

class Create_User_Schema(BaseModel):
    username: str
    email: str
    password: str

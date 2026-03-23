from pydantic import BaseModel

class CreateUserSchema(BaseModel):
    username: str
    email: str
    password: str

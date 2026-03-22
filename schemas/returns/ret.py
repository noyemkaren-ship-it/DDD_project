from pydantic import BaseModel


class Error(BaseModel):
    error_name: str
    message: str

class Message(BaseModel):
    name: str
    text: str
    success: bool

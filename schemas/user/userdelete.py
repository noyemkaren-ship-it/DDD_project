from pydantic import BaseModel

class UserSchemaDelete(BaseModel):
    username: str
    id: int
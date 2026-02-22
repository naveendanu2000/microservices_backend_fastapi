from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str
    age: int
    email: str
    sports: str
    password: str

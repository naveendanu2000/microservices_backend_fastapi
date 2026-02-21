from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    age: int
    email: str
    sports: str
    password: str

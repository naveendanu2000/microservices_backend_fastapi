from pydantic import BaseModel


class PostSchema(BaseModel):
    userid: int
    content: str

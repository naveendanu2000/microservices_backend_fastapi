from pydantic import BaseModel


class CommentSchema(BaseModel):
    content: str
    userid: int
    postid: int

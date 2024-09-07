from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator, Field
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


    class Config:
        from_attributes = True


class Post(PostBase):
    id : int 
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int


class CreateUser(BaseModel):
    email: EmailStr
    password: str




class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: int = Field(default=0)

    @field_validator("dir")
    def validate_vote(cls, value):
        if value not in (0, 1):
            raise ValueError("Vote must be either 0 or 1")
        return value
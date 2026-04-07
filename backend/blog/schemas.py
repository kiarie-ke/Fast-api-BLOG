from typing import List
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str

    class Config:          # indented inside Blog
     from_attributes = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowBlog(BaseModel):
    title: str
    body: str

    class Config:          # indented inside ShowBlog
     from_attributes = True


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[ShowBlog] = []

    class Config:          # indented inside ShowUser
     from_attributes = True


class Login(BaseModel):
   username: str     
   password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None   
from typing import List
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    password: str

class UserListResponse(BaseModel):
    users: List[UserResponse]
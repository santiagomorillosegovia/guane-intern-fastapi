from pydantic import BaseModel
from typing import Optional

class Dog(BaseModel):
    name: str
    picture: Optional[str]
    is_adopted: bool
    create_date: Optional[str]
    id_user: Optional[str]
    
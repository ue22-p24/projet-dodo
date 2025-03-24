import datetime
from typing import Literal
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    content: str
    is_done: bool = False
    created_at: datetime.datetime
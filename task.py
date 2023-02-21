import sqlite3
from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    id: Optional[int]
    description: str
    user: str

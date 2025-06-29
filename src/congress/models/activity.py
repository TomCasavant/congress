from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Activity(BaseModel):
    date: Optional[datetime] = None
    name: Optional[str] = ''

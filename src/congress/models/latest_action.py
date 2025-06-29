from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class LatestAction(BaseModel):
    action_date: Optional[datetime] = Field(None, alias="actionDate")
    text: Optional[str] = ''

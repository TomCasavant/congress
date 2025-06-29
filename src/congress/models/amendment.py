from pydantic import BaseModel, Field
from congress.models.latest_action import LatestAction
from datetime import datetime
from typing import Any, TypeVar, Type, cast, Optional

class Amendment(BaseModel):
    congress: Optional[int] = None
    description: Optional[str] = ''
    latest_action: Optional['LatestAction'] = Field(None, alias="latestAction")
    number: Optional[int] = None
    type: Optional[str] = ''
    update_date: Optional[datetime] = Field(None, alias="updateDate")
    url: Optional[str] = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

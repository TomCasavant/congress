from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any, TypeVar, Type, cast, Optional

class Summary(BaseModel):
    action_date: Optional[datetime] = Field(None, alias="actionDate")
    action_desc: Optional[str] = Field(None, alias='actionDesc')
    text: Optional[str] = None
    update_date: Optional[datetime] = Field(None, alias="updateDate")
    version_code: Optional[str] = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

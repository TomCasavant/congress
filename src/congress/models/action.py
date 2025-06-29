from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any, TypeVar, Type, cast, Optional, List

class SourceSystem(BaseModel):
    code: Optional[int] = None
    name: Optional[str] = None
    
class Action(BaseModel):
    action_code: Optional[str] = Field(None, alias="actionCode")
    action_date: Optional[datetime] = Field(None, alias="actionDate")
    source_system: Optional[SourceSystem] = Field(None, alias="sourceSystem")
    text: Optional[str] = None
    type: Optional[str] = None

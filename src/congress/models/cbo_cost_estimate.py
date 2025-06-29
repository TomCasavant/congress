from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any, TypeVar, Type, cast, Optional, List

class CboCostEstimate(BaseModel):
    description: Optional[str] = None
    pub_date: Optional[datetime] = Field(None, alias="pubDate")
    title: Optional[str]
    url: Optional[str] = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

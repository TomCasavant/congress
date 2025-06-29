from pydantic import BaseModel, Field
from congress.models.activity import Activity
from datetime import datetime
from typing import Any, TypeVar, Type, cast, Optional, List

class Committee(BaseModel):
    activities: List[Activity]
    chamber: Optional[str] = ''
    name: Optional[str] = ''
    system_code: Optional[str] = ''
    type: Optional[str] = ''
    url: Optional[str] = ''

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any, TypeVar, Type, cast, Optional, List

class Format(BaseModel):
    type: Optional[str] = None
    url: Optional[str] = None
        
class TextVersion(BaseModel):
    formats: Optional[List[Format]] = None
    type: Optional[str] = None
    date: Optional[datetime] = None

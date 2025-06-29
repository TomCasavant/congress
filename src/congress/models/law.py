from pydantic import BaseModel
from typing import Any, TypeVar, Type, cast, Optional, List

class Law(BaseModel):
    number: Optional[str] = None
    type: Optional[str] = None

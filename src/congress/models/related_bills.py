from pydantic import BaseModel, Field
from congress.models.latest_action import LatestAction
from datetime import datetime
from typing import Any, TypeVar, Type, cast, Optional, List

class RelationshipDetail(BaseModel):
    identified_by: Optional[str] = Field(None, alias="identifiedBy")
    type: Optional[str] = None

class RelatedBill(BaseModel):
    congress: Optional[int] = None
    latest_action: Optional['LatestAction'] = Field(None, alias="latestAction")
    number: Optional[int] = None
    relationship_details: Optional[List[RelationshipDetail]] = Field(None, alias="relationshipDetails") 
    title: Optional[str] = None
    type: Optional[str] = None
    url: Optional[str] = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

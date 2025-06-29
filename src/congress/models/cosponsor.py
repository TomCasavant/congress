from pydantic import BaseModel, Field
from congress.models.latest_action import LatestAction
from datetime import datetime
from typing import Any, TypeVar, Type, cast, Optional

class Cosponsor(BaseModel):
    bioguide_id: Optional[str] = Field(None, alias="bioguideId")
    district: Optional[int] = None
    first_name: Optional[str] = Field(None, alias="firstName")
    full_name: Optional[str] = Field(None, alias="fullName")
    is_original_cosponsor: Optional[bool] = Field(None, alias="isOriginalCosponsor")
    last_name: Optional[str] = Field(None, alias="lastName")
    party: Optional[str] = None
    sponsorship_date: Optional[str] = Field(None, alias="sponsorshipDate")
    state: Optional[str] = None
    url: Optional[str] = None
    middle_name: Optional[str] = Field(None, alias="middleName")
    

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

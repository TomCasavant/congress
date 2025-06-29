from pydantic import BaseModel, Field
from congress.models.latest_action import LatestAction
from datetime import datetime
from typing import Any, TypeVar, Type, cast, Optional

class Sponsor(BaseModel):
    bioguide_id: Optional[str] = Field(None, alias="bioguideId")
    district: Optional[int] = None
    first_name: Optional[str] = Field(None, alias="firstName")
    full_name: Optional[str] = Field(None, alias="fullName")
    last_name: Optional[str] = Field(None, alias="lastName")
    middle_name: Optional[str] = Field(None, alias="middleName")
    party: Optional[str] = None
    state: Optional[str] = None
    url: Optional[str] = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

class Cosponsor(Sponsor):
    is_original_cosponsor: Optional[bool] = Field(None, alias="isOriginalCosponsor")
    sponsorship_date: Optional[str] = Field(None, alias="sponsorshipDate")

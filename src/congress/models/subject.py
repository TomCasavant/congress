from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any, TypeVar, Type, cast, Optional, List

class PolicyArea(BaseModel):
    name: Optional[str] = ''
    update_date: datetime = Field(None, alias="updateDate")

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

class Subjects(BaseModel):
    legislative_subjects: Optional[List[PolicyArea]] = Field(None, alias="legislativeSubjects")
    policy_area: Optional[PolicyArea] = Field(None, alias="policyArea")

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

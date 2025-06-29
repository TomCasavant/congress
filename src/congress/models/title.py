from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any, TypeVar, Type, cast, Optional

class Title(BaseModel):
    title: Optional[str]
    title_type: Optional[str] = Field(None, alias="titleType")
    title_type_code: Optional[int] = Field(None, alias="titleTypeCode")
    update_date: Optional[datetime] = Field(None, alias="updateDate")
    bill_text_version_code: Optional[str] = Field(None, alias="billTextVersionCode")
    bill_text_version_name: Optional[str] = Field(None, alias="billTextVersionName")
    chamber_code: Optional[str] = Field(None, alias="chamberCode")
    chamber_name: Optional[str] = Field(None, alias="chamberName")

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

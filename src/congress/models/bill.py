from pydantic import BaseModel, Field, PrivateAttr
from datetime import datetime
from typing import Any, TypeVar, Type, cast, Optional, List, Dict
import dateutil.parser
from congress.rest_adapter import RestAdapter
from functools import cached_property
from congress.models.amendment_result import AmendmentsResult
from congress.models.committees_result import CommitteesResult
from congress.models.cosponsors_result import CosponsorsResult
from congress.models.related_bills_result import RelatedBillsResult
from congress.models.subjects_result import SubjectsResult
from congress.models.summaries_result import SummariesResult
from congress.models.text_result import TextResult
from congress.models.titles_result import TitlesResult
from congress.models.latest_action import LatestAction
from congress.models.actions_result import ActionsResult

class Bill(BaseModel):
    _rest_adapter: Optional[RestAdapter] = PrivateAttr(default=None)

    congress: Optional[int] = None
    latest_action: Optional['LatestAction'] = Field(None, alias="latestAction")
    number: Optional[int] = None
    origin_chamber: Optional[str] = Field('', alias="originChamber")
    origin_chamber_code: Optional[str] = Field('', alias="originChamberCode")
    title: Optional[str] = ''
    type: Optional[str] = ''
    update_date: Optional[datetime] = Field(None, alias="updateDate")
    update_date_including_text: Optional[datetime] = Field(None, alias="updateDateIncludingText")
    url: Optional[str] = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

    def set_rest_adapter(self, adapter: RestAdapter):
        self._rest_adapter = adapter

    def _get_endpoint(self, suffix: str):
        if not self._rest_adapter:
            raise RuntimeError("Rest adapter not set on Bill")
        if not all([self.type, self.number, self.congress]):
            raise ValueError("Bill object missing required info for endpoint")
        endpoint = f"/bill/{self.congress}/{self.type.lower()}/{self.number}/{suffix}"
        return self._rest_adapter.get(endpoint=endpoint)

    @cached_property
    def actions(self):
        return ActionsResult.from_result(self._get_endpoint("actions"), self._rest_adapter)
        
    @cached_property
    def committees(self):
        return CommitteesResult.from_result(self._get_endpoint("committees"), self._rest_adapter)
    
    @cached_property
    def cosponsors(self):
        return CosponsorsResult.from_result(self._get_endpoint("cosponsors"), self._rest_adapter)
    
    @cached_property
    def related_bills(self):
        return RelatedBillsResult.from_result(self._get_endpoint("relatedbills"), self._rest_adapter)
    
    @cached_property
    def subjects(self):
        return SubjectsResult.from_result(self._get_endpoint("subjects"), self._rest_adapter)
    
    @cached_property
    def summaries(self):
        return SummariesResult.from_result(self._get_endpoint("summaries"), self._rest_adapter)
    
    @cached_property
    def titles(self):
        return TitlesResult.from_result(self._get_endpoint("titles"), self._rest_adapter)
    
    @cached_property
    def text(self):
        return TextResult.from_result(self._get_endpoint("text"), self._rest_adapter)

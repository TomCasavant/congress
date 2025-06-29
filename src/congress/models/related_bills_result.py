from congress.models.result import ListResult, Result
from congress.models.related_bills import RelatedBill
from typing import Dict

class RelatedBillsResult(ListResult[RelatedBill]):
    def __init__(self, status_code: int, message: str = "", data: Dict = None, rest_adapter = None):
        super().__init__(status_code, message, data, rest_adapter)

        if data and 'relatedBills' in data:
            self._items = [RelatedBill(**bill_data) for bill_data in data['relatedBills']]

    @classmethod
    def from_result(cls, result: Result, rest_adapter = None):
        return cls(
            status_code=result.status_code,
            message=result.message,
            data=result.data,
            rest_adapter=rest_adapter
        )

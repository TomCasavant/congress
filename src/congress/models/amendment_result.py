from congress.models.result import ListResult, Result
from congress.models.amendment import Amendment
from typing import Dict, List

class AmendmentsResult(ListResult[Amendment]):
    def __init__(self, status_code: int, message: str = "", data: Dict = None, rest_adapter = None):
        super().__init__(status_code, message, data, rest_adapter)

        if data and 'amendments' in data:
            self._items = [Amendment(**amendment_data) for amendment_data in data['amendments']]

    @classmethod
    def from_result(cls, result: Result, rest_adapter = None):
        return cls(
            status_code=result.status_code,
            message=result.message,
            data=result.data,
            rest_adapter=rest_adapter
        )

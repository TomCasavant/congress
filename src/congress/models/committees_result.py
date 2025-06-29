from congress.models.result import ListResult, Result
from congress.models.committee import Committee
from typing import Dict

class CommitteesResult(ListResult[Committee]):
    def __init__(self, status_code: int, message: str = "", data: Dict = None, rest_adapter = None):
        super().__init__(status_code, message, data, rest_adapter)

        if data and 'committees' in data:
            self._items = [Committee(**committee_data) for committee_data in data['committees']]

    @classmethod
    def from_result(cls, result: Result, rest_adapter = None):
        return cls(
            status_code=result.status_code,
            message=result.message,
            data=result.data,
            rest_adapter=rest_adapter
        )

from congress.models.result import ListResult, Result
from congress.models.title import Title
from typing import Dict, List

class TitlesResult(ListResult[Title]):
    def __init__(self, status_code: int, message: str = "", data: Dict = None, rest_adapter = None):
        super().__init__(status_code, message, data)
        if data and 'titles' in data:
            self._items = [Title(**title_data) for title_data in data['titles']]

    @classmethod
    def from_result(cls, result: Result, rest_adapter = None):
        return cls(
            status_code=result.status_code,
            message=result.message,
            data=result.data,
            rest_adapter=rest_adapter
        )

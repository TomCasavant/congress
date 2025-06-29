from congress.models.result import ListResult, Result
from congress.models.cosponsor import Cosponsor
from typing import Dict

class CosponsorsResult(ListResult[Cosponsor]):
    def __init__(self, status_code: int, message: str = "", data: Dict = None, rest_adapter = None):
        super().__init__(status_code, message, data, rest_adapter)

        if data and 'cosponsors' in data:
            self._items = [Cosponsor(**cosponsor_data) for cosponsor_data in data['cosponsors']]

    @classmethod
    def from_result(cls, result: Result, rest_adapter = None):
        return cls(
            status_code=result.status_code,
            message=result.message,
            data=result.data,
            rest_adapter=rest_adapter
        )

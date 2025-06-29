from congress.models.result import ListResult, Result
from congress.models.action import Action
from typing import Dict

class ActionsResult(ListResult[Action]):
    def __init__(self, status_code: int, message: str = "", data: Dict = None, rest_adapter = None):
        super().__init__(status_code, message, data, rest_adapter)
        if data and 'actions' in data:
            self._items = [Action(**action) for action in data['actions']]

    @classmethod
    def from_result(cls, result: Result, rest_adapter = None):
        return cls(
            status_code=result.status_code,
            message=result.message,
            data=result.data,
            rest_adapter=rest_adapter
        )

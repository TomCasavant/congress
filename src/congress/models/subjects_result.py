from congress.models.result import Result
from congress.models.subject import Subjects
from typing import Dict

class SubjectsResult(Result):
    def __init__(self, status_code: int, message: str = "", data: Dict = None, rest_adapter = None):
        super().__init__(status_code, message, data, rest_adapter)
        self.subjects: List[Subject] = []

        if data and 'subjects' in data:
            self.subjects = Subjects(**data['subjects'])

    @classmethod
    def from_result(cls, result: Result, rest_adapter = None):
        return cls(
            status_code=result.status_code,
            message=result.message,
            data=result.data,
            rest_adapter=rest_adapter
        )

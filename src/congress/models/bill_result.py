from dataclasses import dataclass
from typing import Dict, List
from congress.models.bill import Bill
from congress.rest_adapter import RestAdapter
from congress.models.result import ListResult, Result

class BillResult(ListResult[Bill]):
    """
    Result subclass for bill-specific responses.
    Behaves like a list of Bill objects from the data['bills'] field.
    """

    def __init__(self, status_code: int, message: str = "", data: Dict = None, rest_adapter: RestAdapter = None):
        super().__init__(status_code, message, data, rest_adapter)

        if data and 'bills' in data:
            self._items = []
            for bill_data in data['bills']:
                bill = Bill(**bill_data)
                if rest_adapter:
                    bill.set_rest_adapter(rest_adapter)
                self._items.append(bill)

    @classmethod
    def from_result(cls, result: Result, rest_adapter: RestAdapter = None):
        return cls(
            status_code=result.status_code,
            message=result.message,
            data=result.data,
            rest_adapter=rest_adapter
        )

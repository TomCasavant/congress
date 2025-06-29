from dataclasses import dataclass
from typing import Dict, Generic, TypeVar, Iterator, List, Optional

T = TypeVar("T")

class Result:
    """
    """
    _rest_adapter: Optional["RestAdapter"] = None

    _next_page: str = None
    _count: int = None
    _congress: str = None
    _content_type: str = None
    _format: str = None
    _bill_number: str = None
    _bill_url: str = None
    _bill_type: str = None

    def __init__(self, status_code: int, message: str = "", data: Dict = None, rest_adapter = None):
        """
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data
        self._rest_adapter = rest_adapter

        print(self.data)

        if data:   
            pagination = data.get('pagination', {})
            self._next_page = str(pagination.get('next'))
            self._count = int(pagination.get('count', 0))

            req = data.get('request', {})
            self._congress = str(req.get('congress', ''))
            self._content_type = str(req.get('ContentType', ''))
            self._format = str(req.get('format', ''))
            
            self._bill_number = str(req.get('billNumber', ''))
            self._bill_url = str(req.get('billUrl', ''))
            self._bill_type = str(req.get('billType', ''))

    def next(self) -> "Result":
        """
        Fetch the next page of results if available.
        Returns a new Result instance for the next page.
        Raises an exception or returns None if no next page.
        """
        if not self._next_page or not self._rest_adapter:
            return None  # or raise StopIteration or custom exception


        response = self._rest_adapter.get(self._next_page)  # or parse _next_page to endpoint
        return self.__class__(response.status_code, response.message, response.data)
            
class ListResult(Result, Generic[T]):
    _items: List[T] = []

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        max_display = 3
        items_preview = ", ".join(repr(item) for item in self._items[:max_display])
        if len(self._items) > max_display:
            items_preview += ", ..."
        return f"<{self.__class__.__name__} [{items_preview}]>"

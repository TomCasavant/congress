import logging
from .rest_adapter import RestAdapter
from congress.models.bill_result import BillResult
from congress.models.bill import Bill

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

class CongressClient:
    """
    """

    CURRENT_CONGRESS = 118

    def __init__(self, api_key: str, hostname: str = "api.congress.gov", ver: str = "v3", ssl_verify: bool = True, logger: logging.Logger = None):
        """
        """
        self._rest_adapter = RestAdapter(hostname, api_key, ver, ssl_verify, logger)

    def get_bills(self, bill_type: str = None, bill_number: int = None, congress: int = None):
        if not congress:
            congress = self.CURRENT_CONGRESS

        if bill_number is not None and bill_type is None:
            raise ValueError("bill_number cannot be used without bill_type")

        endpoint = f"/bill/{congress}"
        if bill_type is not None:
            endpoint += f"/{bill_type}"
        if bill_number is not None:
            endpoint += f"/{bill_number}"

        return BillResult.from_result(self._rest_adapter.get(endpoint=endpoint), self._rest_adapter)

    def get_bill(self, bill_type: str, bill_number: int, congress: int = None) -> Bill:
        if congress is None:
            congress = self.CURRENT_CONGRESS
    
        if not bill_type or not bill_number:
            raise ValueError("bill_type and bill_number are required for get_bill")
    
        endpoint = f"/bill/{congress}/{bill_type}/{bill_number}"
        result = self._rest_adapter.get(endpoint=endpoint)
        bill_data = result.data.get("bill")
    
        if not bill_data:
            raise ValueError(f"No bill data found for {congress}/{bill_type}/{bill_number}")
    
        bill = Bill(**bill_data)
        bill.set_rest_adapter(self._rest_adapter)
        return bill
    

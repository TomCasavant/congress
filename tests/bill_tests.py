import os
import pytest
from congress.congress_client import CongressClient
from congress.models.bill import Bill
from congress.models.result import BillResult

SAMPLE_BILL = {
    'congress': 119,
    'latestAction': {
        'actionDate': '2025-06-26',
        'text': 'Read twice and referred to the Committee on the Judiciary.'
    },
    'number': '2191',
    'originChamber': 'Senate',
    'originChamberCode': 'S',
    'title': 'A bill to amend title 18, United States Code, to prevent bulk sales of ammunition, promote recordkeeping and reporting about ammunition, end ammunition straw purchasing, and require a background check before the transfer of ammunition by certain Federal firearms licensees to non-licensees.',
    'type': 'S',
    'updateDate': '2025-06-27',
    'updateDateIncludingText': '2025-06-27',
    'url': 'https://api.congress.gov/v3/bill/119/s/2191?format=json'
}

SAMPLE_BILL_RESULT_DATA = {
    'status_code': 200,
    'message': 'Success',
    'data': {
        'pagination': {'next': None, 'count': 1},
        'request': {
            'congress': 119,
            'ContentType': 'application/json',
            'format': 'json'
        },
        'bills': [SAMPLE_BILL]
    }
}

@pytest.fixture
def client():
    api_key = os.getenv('CONGRESS_API_KEY', 'dummy_key_for_tests')
    return CongressClient(api_key=api_key)

def test_get_bills(mocker, client):
    mocker.patch.object(client._rest_adapter, 'get', return_value=SAMPLE_BILL_RESULT_DATA)
    
    bills_result = client.get_bills()
    
    assert isinstance(bills_result, BillResult)
    assert len(bills_result.bills) > 0

def test_get_bill_with_params(mocker, client):
    mocker.patch.object(client._rest_adapter, 'get', return_value=SAMPLE_BILL_RESULT_DATA)
    
    # Test with congress, bill_type, and bill_number
    result = client.get_bill(bill_type='s', bill_number='2191', congress=119)
    assert isinstance(result, BillResult)
    assert result.bills[0].number == 2191

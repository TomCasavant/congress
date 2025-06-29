# Congress
## Python wrapper for congress API

### Examples

#### Initialize Client
```python
from congress.congress_client import CongressClient
congress = CongressClient(api_key="API_KEY_HERE")
```

#### Bill Endpoints

Bills by congress
```python
bills = congress.get_bills(congress=119) # -> List of Bill Objects
```

Bills by congress and house
```python
bills = congress.get_bills(congress=119, bill_type="hr")
```

Bill by Bill number
```python
bill = congress.get_bill(congress=119, bill_type="hr", bill_number=1) # -> Individual Bill Object
```

Bill attributes
```python
print(bill.actions) # -> List of Actions
print(bill.committees) # -> List of Committees
print(bill.cosponsors) # -> List of Cosponsors
print(bill.related_bills) # -> List of Related Bills
print(bill.subjects) # -> List of Subjects
print(bill.summaries) # -> List of bill Summaries
print(bill.titles) # -> List of bill Titles
print(bill.text) # -> List of bill TextVersions
```

Bill Pagination
```python
bills = congress.get_bills(congress=119) # -> List of Bill Objects
bills_next_page = bills.next() # -> The next page of Bill Objects
```

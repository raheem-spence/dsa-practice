# REST API OA Notes

## Core Idea

A REST API problem is usually just:

API call → JSON response → collect records → filter/count/sort → return answer

The API is the input source. Once I collect the data, it becomes a normal list/dictionary problem.

---

## Basic Request

```python
import requests

response = requests.get(url, params={"page": 1})
data = response.json()
```

Meaning:
- requests.get(...) sends a GET request to the API
- response is a Response object
- response.json() converts the JSON response body into Python data, usually a dictionary

## Common Response Shape
```json
{
    "page": 1,
    "per_page": 10,
    "total": 100,
    "total_pages": 10,
    "data": [
        {...},
        {...}
    ]
}
```

Important keys:
- `total_pages` tells me how many pages I need to request
- `data` usually contains the actual list of record

## Pagination Pattern
1. Request page 1
2. Convert response with `.json()`
3. Get `total_pages`
4. Store page 1 records
5. Loop from page 2 to `total_pages`
6. Extend `all records`
7. Solve the actual problem using normal loops

```python
import requests

def get_all_records(url, params=None):
    if params is None:
        params = {}

    response = requests.get(url, params={**params, "page": 1})
    data = response.json()

    total_pages = data.get("total_pages", 1)
    all_records = data.get("data", [])

    for page in range(2, total_pages + 1):
        response = requests.get(url, params={**params, "page": page})
        data = response.json()
        all_records.extend(data.get("data", []))

    return all_records
```

## Why Page 1 First?

Page 1 gives me:
- the first records
- the `total_pages` value

That is why the loop starts at page 2.
```python
for page in range(2, total_pages + 1):
```

Use `total_pages + 1` because Python `range` excludes the end.

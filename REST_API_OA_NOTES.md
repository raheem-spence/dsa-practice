# REST API OA Notes

## What is a REST API?

A REST API is a way for programs to communicate over the internet using HTTP requests.

In an OA problem, the API usually acts as the input source. Instead of receiving an array directly, I call a URL, get data back, convert it from JSON into Python data, and then solve the problem normally.

Common HTTP methods:
- `GET` = retrieve data
- `POST` = create/send data
- `PUT` / `PATCH` = update data
- `DELETE` = delete data

For HackerRank REST API questions, I will usually use `GET`.

Example:

```python
response = requests.get(url, params={"page": 1})
data = response.json()
```

Meaning:

- `requests.get(...)` sends a GET request to the API
- `params={...}` adds query parameters to the URL
- `response` is the HTTP response object
- `response.json()` converts the JSON response body into Python data


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

## append() vs extend()

Use `append()` when adding one item:
```python
names.append(record.get("name"))
```

Use `extend()` when adding all items from another list:
```python
all_records.extend(data.get("data", []))
```
```python
Example:

a = [1, 2]
b = [3, 4]

a.append(b)
# [1, 2, [3, 4]]

a.extend(b)
# [1, 2, 3, 4]
```

For pagination, use `extend()` because each page gives a list of records.


## Common Operations
### Filter and return names
```python
result = []

for record in all_records:
    if record.get("population") > threshold:
        result.append(record.get("name"))

result.sort()
return result
```
### Count matching records
```python
count = 0

for record in all_records:
    if record.get("field") == target:
        count += 1

return count
```
### Return sorted titles
```python
titles = []

for record in all_records:
    titles.append(record.get("Title"))

return sorted(titles)
```

## Mistakes to Avoid
- Forgetting pagination
- Forgetting to include query params on every page request
- Starting at page 0 instead of page 1
- Using the wrong JSON key, like results instead of data
- Returning full records when the prompt asks for names/titles only
- Getting field capitalization wrong, like title instead of Title
- Returning `list.sort(`) because `.sort()` returns `None`
- Using `append()` when I need `extend()`

## Mental Model

REST API OA problem = fetch all input first, then solve like a normal array/list problem.

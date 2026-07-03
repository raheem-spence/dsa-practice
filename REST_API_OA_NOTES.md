# REST API OA Notes

## 1. What is a REST API?

A REST API lets my code request data from a server using HTTP.

In HackerRank/OA problems, the API is usually the input source. Instead of getting an array directly, I call a URL, get JSON back, convert it into Python dictionaries/lists, and solve the problem normally.

Mental model:

```text
REST API problem = fetch input from URL → parse JSON → loop/filter/sort/count → return answer
```

---

## 2. Basic Request

```python
import requests

response = requests.get(url, params={"page": 1})
data = response.json()
```

Meaning:
- `requests.get(...)` sends a GET request to the API
- `params={...}` adds query parameters to the URL
- `response` is a Response object
- `response.json()` converts the JSON response body into Python data

---

## 3. Query Parameters

Query parameters are key-value pairs added to a URL after a `?`.

Example:

```text
https://jsonmock.hackerrank.com/api/movies/search/?Title=spiderman&page=1
```

Query params:

```text
Title=spiderman
page=1
```

Meaning:
- `Title=spiderman` searches for movies with `"spiderman"` in the title
- `page=1` asks for the first page of results

In Python:

```python
response = requests.get(url, params={"Title": substr, "page": 1})
```

Mental model:

```text
base URL = where the API lives
query params = what specific data I want
```

---

## 4. Pagination

Pagination means an API sends data in pages/batches instead of sending everything at once.

Example:
- Page 1 = first 10 records
- Page 2 = next 10 records
- Page 3 = next 10 records

Common response shape:

```json
{
  "page": 1,
  "per_page": 10,
  "total": 100,
  "total_pages": 10,
  "data": [
    {
      "name": "India",
      "region": "Asia",
      "population": 1380004385
    }
  ]
}
```

Important keys:
- `page` = current page
- `per_page` = records per page
- `total` = total records
- `total_pages` = how many pages exist
- `data` = records on the current page

Mental model:

```text
The API gives me one page at a time.
I request page 1 first, read total_pages, then loop through the rest.
```

---

## 5. Pagination Pattern

Steps:
1. Store the base URL
2. Request page 1
3. Convert response with `.json()`
4. Get `total_pages`
5. Store page 1 records
6. Loop from page 2 to `total_pages`
7. Extend all records
8. Filter/count/sort/extract based on the prompt
9. Return the exact requested output

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

Why start at page 2?

```text
Page 1 is already collected before the loop.
```

Why `total_pages + 1`?

```text
Python range excludes the end.
range(2, total_pages + 1) includes the final page.
```

---

## 6. `append()` vs `extend()`

Use `append()` when adding one item:

```python
names.append(record.get("name"))
```

Use `extend()` when adding all items from another list:

```python
all_records.extend(data.get("data", []))
```

Example:

```python
a = [1, 2]
b = [3, 4]

a.append(b)
# [1, 2, [3, 4]]

a.extend(b)
# [1, 2, 3, 4]
```

Mental model:

```text
append = add one thing
extend = add each item from another list
```

---

## 7. Common Operations

### Filter and return names

```python
result = []

for record in all_records:
    if record.get("population") > threshold:
        result.append(record.get("name"))

result.sort()
return result
```

### Return sorted titles

```python
titles = []

for record in all_records:
    titles.append(record.get("Title"))

return sorted(titles)
```

### Count matching records

```python
count = 0

for record in all_records:
    if record.get("field") == target:
        count += 1

return count
```

---

## 8. Mistakes to Avoid

- Forgetting pagination
- Forgetting to include query params on every page request
- Starting at page 0 instead of page 1
- Using the wrong JSON key, like `results` instead of `data`
- Returning full records when the prompt asks for names/titles only
- Getting field capitalization wrong, like `title` instead of `Title`
- Returning `list.sort()` because `.sort()` returns `None`
- Using `append()` when I need `extend()`
- Forgetting that `response` is a Response object; `response.json()` gives me Python data

---

## 9. Final Mental Model

```text
API gives me the input.
The input may be split across pages.
Fetch all pages first.
Then solve like a normal list/dictionary problem.
```

# Exercise 03 — Fast User Lookup

## Problem

Given a collection of users, find a user using their `user_id`.

The exercise compares two approaches:

- sequential lookup in a list;
- lookup through a dictionary index.

## Input

```python
users = [
    {"user_id": "u1", "name": "Alice"},
    {"user_id": "u2", "name": "Bob"},
    {"user_id": "u3", "name": "Charlie"},
]
```

## Expected Output

```python
{"user_id": "u2", "name": "Bob"}
```

When the requested user does not exist, the function returns:

```python
None
```

For this exercise, `user_id` values are assumed to be unique.

## V1 — Sequential Lookup in a List

The first version iterates through the list until it finds a matching `user_id`.

```python
def find_user_by_id_v1(
    users: list[dict[str, str]],
    target_user_id: str,
) -> dict[str, str] | None:
```

### Complexity

- Best case: **O(1)**, when the user is the first element.
- Average case: **O(n)**.
- Worst case: **O(n)**, when the user is the last element or does not exist.
- Additional space: **O(1)**.

## V2 — Lookup with a Dictionary Index

The second version first builds an index:

```python
{
    "u1": {"user_id": "u1", "name": "Alice"},
    "u2": {"user_id": "u2", "name": "Bob"},
    "u3": {"user_id": "u3", "name": "Charlie"},
}
```

The index is built once:

```python
def build_user_index(
    users: list[dict[str, str]],
) -> dict[str, dict[str, str]]:
```

Then users can be retrieved directly:

```python
def find_user_by_id_v2(
    user_index: dict[str, dict[str, str]],
    target_user_id: str,
) -> dict[str, str] | None:
```

### Complexity

- Index construction: **O(n)** time and **O(n)** space.
- Dictionary lookup: **O(1)** on average.

## Benchmark

The benchmark searches for the last user in each list, which represents the worst case for the sequential lookup.

Each lookup is repeated 1,000 times and the table reports the average lookup time.

| Users | Index build | List lookup | Dictionary lookup |
|---:|---:|---:|---:|
| 10 | 2.44 µs | 0.62 µs | 0.12 µs |
| 100 | 13.50 µs | 4.36 µs | 0.10 µs |
| 1,000 | 144.39 µs | 38.06 µs | 0.08 µs |
| 10,000 | 843.76 µs | 333.15 µs | 0.08 µs |

## Results

The list lookup grows as the number of users increases. This is consistent with **O(n)** time complexity.

The dictionary lookup remains almost constant as the dataset grows. This is consistent with **O(1)** average lookup time.

However, building the dictionary index has an initial **O(n)** cost.

For a single lookup, especially near the beginning of a small list, a sequential search can be sufficient.

When the same collection is queried repeatedly, building an index is more efficient.

## Tests

The test suite verifies:

- a user at the beginning, middle, and end of the list;
- a missing user;
- an empty list;
- an element without `user_id`, which raises `KeyError`.

Run the tests with:

```bash
python -m pytest -v
```

Run the benchmark with:

```bash
python benchmark.py
```

## What I Learned

- A list is appropriate for sequential traversal.
- A dictionary is useful when fast lookup by key is required.
- Building an index has an upfront cost.
- The right data structure depends on how often the data is queried.
- Benchmarks must measure each operation separately.
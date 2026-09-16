# Exercise 02 — Aggregate Events by User

## Problem

Given a list of events, calculate the total duration associated with each user.

Each event contains:

- `user_id`: the identifier of the user;
- `duration`: the duration associated with the event.

## Input

```python
events = [
    {"user_id": "u1", "duration": 10},
    {"user_id": "u2", "duration": 5},
    {"user_id": "u1", "duration": 7},
    {"user_id": "u3", "duration": 4},
    {"user_id": "u2", "duration": 8},
]
```

## Expected Output

```python
{
    "u1": 17,
    "u2": 13,
    "u3": 4,
}
```

## V1 — Explicit Initialization with `if`

The first version explicitly checks whether the user already exists in the dictionary.

If the user does not exist, its total duration is initialized to `0`.

This version is explicit and easy to understand.

## V2 — Aggregation with `dict.get()`

The second version uses:

```python
total_duration_by_user.get(user_id, 0)
```

If `user_id` is present, `get()` returns its current total. Otherwise, it returns `0`.

This version is more compact and does not require additional imports.

## V3 — Aggregation with `defaultdict`

The third version uses:

```python
defaultdict(int)
```

When a key does not exist, `int()` provides the default value `0`.

This version is concise and particularly useful for repeated aggregations.

## Time and Space Complexity

For all three versions:

- Time complexity: **O(n)**, because the events are traversed once.
- Space complexity: **O(k)**, where `k` is the number of distinct users.
- Dictionary lookup and update: **O(1)** on average.

## Tests

The test suite verifies:

- aggregation of multiple events;
- an empty list of events;
- a missing `user_id`;
- a missing `duration`;
- an event with both fields missing.

Missing required fields raise a `KeyError`.

Run the tests with:

```bash
python -m pytest -v
```

## What I Learned

In this exercise, I learned:

- how to initialize the value of a new dictionary key;
- how to aggregate values by key;
- how to use `dict.get()` with a default value;
- how `defaultdict(int)` initializes missing keys to `0`;
- how different implementations can have the same time and space complexity;
- how to test expected exceptions with `pytest.raises()`.
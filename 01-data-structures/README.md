# 01 — Data Structures

## Objectives

Understand the main Python data structures and how choosing the correct structure affects code simplicity, correctness, and performance.

Topics covered in this module:

* `list`
* `tuple`
* `set`
* `dict`
* `deque`
* `heapq`
* Hashing and membership lookup
* FIFO and LIFO processing
* Priority queues
* Time and space complexity
* Tests and benchmarks

## Exercises

|  # | Exercise                 | Main data structures  | Main lesson                                                     |
| -: | ------------------------ | --------------------- | --------------------------------------------------------------- |
| 01 | Find Duplicate Events    | `list`, `set`         | A set makes duplicate detection scale from `O(n²)` to `O(n)`.   |
| 02 | Aggregate Events by User | `dict`, `defaultdict` | Dictionaries are efficient hash maps for aggregation by key.    |
| 03 | Fast User Lookup         | `list`, `dict`        | Building an index makes repeated lookups much faster.           |
| 04 | FIFO Event Queue         | `list`, `deque`       | `deque.popleft()` is more efficient than `list.pop(0)`.         |
| 05 | LIFO Event Stack         | `list`                | `list.append()` and `list.pop()` efficiently implement a stack. |
| 06 | Priority Event Queue     | `list`, `heapq`       | A heap efficiently retrieves the next highest-priority event.   |

---

## Exercise 01 — Find Duplicate Events

Given a collection of events, find the `event_id` values that occur more than once.

### List-based approach

The first implementation uses `list.count()` for each event ID.

```text
n events × O(n) count = O(n²)
```

### Set-based approach

The improved implementation uses:

```python
seen = set()
duplicates = set()
```

Set membership and insertion are `O(1)` on average.

```text
n events × O(1) lookup = O(n)
```

### Benchmark

| Events | List `O(n²)` | Set `O(n)` |
| -----: | -----------: | ---------: |
|  1,000 |   0.024766 s | 0.000224 s |
|  5,000 |   0.660288 s | 0.000963 s |
| 10,000 |   2.669392 s | 0.001778 s |
| 20,000 |  10.866564 s | 0.004692 s |

---

## Exercise 02 — Aggregate Events by User

Aggregate event durations by `user_id`.

```python
events = [
    {"user_id": "u1", "duration": 10},
    {"user_id": "u2", "duration": 5},
    {"user_id": "u1", "duration": 7},
]
```

Expected result:

```python
{"u1": 17, "u2": 5}
```

Three implementations were explored:

1. Explicit initialization with `if`;
2. `dict.get()`;
3. `defaultdict(int)`.

All three versions have:

```text
Time  → O(n)
Space → O(k)
```

Where `n` is the number of events and `k` is the number of distinct users.

---

## Exercise 03 — Fast User Lookup

Find a user by `user_id`.

### V1 — Linear search

The first version scans a list until it finds the requested user.

```text
Lookup → O(n)
```

### V2 — Dictionary index

The improved version builds an index:

```python
users_index = {
    user["user_id"]: user
    for user in users
}
```

```text
Build index → O(n)
Lookup      → O(1) on average
```

### Benchmark

|  Users |  Build index |  List lookup | Dictionary lookup |
| -----: | -----------: | -----------: | ----------------: |
|     10 | 0.00000244 s | 0.00000062 s |      0.00000012 s |
|    100 | 0.00001350 s | 0.00000436 s |      0.00000010 s |
|  1,000 | 0.00014439 s | 0.00003806 s |      0.00000008 s |
| 10,000 | 0.00084376 s | 0.00033315 s |      0.00000008 s |

Building an index has an initial cost, but it is valuable when the system performs many lookups on the same collection of users.

---

## Exercise 04 — FIFO Event Queue

A FIFO queue follows this rule:

```text
First In, First Out
```

### V1 — `list.pop(0)`

Removing the first element of a list requires shifting the remaining elements.

```text
Remove one event → O(n)
Process n events → O(n²)
```

### V2 — `deque.popleft()`

`deque` is designed for efficient operations at both ends.

```text
Remove one event → O(1)
Process n events → O(n)
```

### Benchmark

| Events |  List `pop(0)` | `deque.popleft()` |
| -----: | -------------: | ----------------: |
|     10 | 0.0000017760 s |    0.0000019016 s |
|    100 | 0.0000279202 s |    0.0000202110 s |
|  1,000 | 0.0001163052 s |    0.0000480954 s |
| 10,000 | 0.0062832778 s |    0.0005421280 s |

With 10,000 events, `deque` was approximately 11.6 times faster.

---

## Exercise 05 — LIFO Event Stack

A LIFO stack follows this rule:

```text
Last In, First Out
```

A Python list efficiently implements a stack:

```python
stack.append(event)  # push
stack.pop()          # pop
```

```text
append()         → O(1) on average
pop()            → O(1)
Process n events → O(n)
Space            → O(n)
```

Typical use cases include undo functionality, parsing nested structures, depth-first search, backtracking, rollback logic, and resource cleanup.

---

## Exercise 06 — Priority Event Queue

A priority queue processes the most important event first.

For this exercise:

```text
priority 1 → highest priority
priority 3 → lowest priority
```

When two events have the same priority, their arrival order is preserved.

### V1 — List-based priority queue

For every extraction, the implementation scans the list to find the lowest priority.

```text
Process n events → O(n²)
```

### V2 — Heap-based priority queue

The improved version uses `heapq` with tuples in this format:

```python
(priority, insertion_order, event)
```

```text
Insert one event  → O(log n)
Extract one event → O(log n)
Process n events  → O(n log n)
```

### Benchmark

| Events |       List |    `heapq` |
| -----: | ---------: | ---------: |
|    100 | 0.000644 s | 0.000051 s |
|    500 | 0.017883 s | 0.000375 s |
|  1,000 | 0.069192 s | 0.000573 s |
|  2,000 | 0.276373 s | 0.001129 s |

With 2,000 events, `heapq` was approximately 244.8 times faster than the list-based implementation.

---

## Choosing the Right Data Structure

| Requirement                                       | Recommended structure | Typical complexity            |
| ------------------------------------------------- | --------------------- | ----------------------------- |
| Keep an ordered collection and access by position | `list`                | Index access: `O(1)`          |
| Store immutable fixed values                      | `tuple`               | Index access: `O(1)`          |
| Check membership or remove duplicates             | `set`                 | Lookup: `O(1)` average        |
| Map a key to a value or aggregate by key          | `dict`                | Lookup/update: `O(1)` average |
| Process items in FIFO order                       | `deque`               | `popleft()`: `O(1)`           |
| Process items in LIFO order                       | `list`                | `pop()`: `O(1)`               |
| Repeatedly process the highest-priority item      | `heapq`               | Push/pop: `O(log n)`          |

## Main Takeaways

* The correct data structure can improve both readability and scalability.
* Repeating an `O(n)` operation inside a loop often produces an `O(n²)` algorithm.
* Hash-based structures such as `set` and `dict` provide `O(1)` average lookup.
* A `deque` should be preferred over a list for FIFO processing.
* A list is already efficient for LIFO stacks.
* A heap is useful for dynamic priority-based scheduling.
* Tests verify correctness; benchmarks validate scalability assumptions.

## Next Module

The next module is:

```text
02 — Big O & Complexity
```

It will formalize the complexity patterns explored here and apply them to nested loops, algorithm comparisons, time-space trade-offs, binary search, and data-pipeline design decisions.

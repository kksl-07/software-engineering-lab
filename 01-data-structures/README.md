# 01 - Data Structures

## Objectives

Understand the main Python data structures and learn how choosing the right data structure affects algorithm performance and code simplicity.

Topics covered in this module:

- `list`
- `tuple`
- `set`
- `dict`
- Membership lookup
- Hashing
- Duplicate detection

---

## Exercise 01 - Find Duplicate Events

Given a collection of events:

```python
events = [
    {"event_id": "e1", "user_id": "u1", "amount": 20},
    {"event_id": "e2", "user_id": "u2", "amount": 10},
    {"event_id": "e1", "user_id": "u1", "amount": 20},
    {"event_id": "e3", "user_id": "u1", "amount": 50},
    {"event_id": "e2", "user_id": "u2", "amount": 10},
]
```

find the event IDs that occur more than once.

Expected result:

```python
["e1", "e2"]
```

### V1 - List-based solution

The first implementation uses lists and `list.count()` to detect duplicates.

The important operation is:

```python
event_ids_list.count(event_id)
```

`list.count()` scans the list and therefore has **O(n)** time complexity.

Since it is executed for every element, the overall algorithm has:

```text
n elements × O(n) count
        =
      O(n²)
```

### V2 - Set-based solution

The improved implementation uses two sets:

```python
seen = set()
duplicates = set()
```

For each event:

1. Check whether the `event_id` is already in `seen`.
2. If it is, add it to `duplicates`.
3. Otherwise, add it to `seen`.

Set membership and insertion have an average time complexity of **O(1)**.

Therefore:

```text
n elements × O(1)
        =
       O(n)
```

---

## Benchmark

The two implementations were benchmarked using `time.perf_counter()`.

Results from the local execution:

| Events | List O(n²) | Set O(n) |
|---:|---:|---:|
| 1,000 | 0.024766 s | 0.000224 s |
| 5,000 | 0.660288 s | 0.000963 s |
| 10,000 | 2.669392 s | 0.001778 s |
| 20,000 | 10.866564 s | 0.004692 s |

One particularly useful observation is what happens when the input doubles from 10,000 to 20,000 events.

The list implementation goes from approximately:

```text
2.67 s → 10.87 s
```

The input increased by **2x**, while execution time increased by approximately **4x**.

This is consistent with quadratic **O(n²)** growth.

The set-based implementation scales much closer to linearly.

---

## What I Learned

### Lists

Searching for an element in a list:

```python
value in my_list
```

requires scanning elements and is therefore **O(n)** in the worst case.

Operations such as:

```python
my_list.count(value)
```

are also **O(n)**.

Using these operations inside another loop can easily produce an **O(n²)** algorithm.

### Sets

Sets are implemented using hashing.

Membership:

```python
value in my_set
```

and insertion:

```python
my_set.add(value)
```

are **O(1) on average**.

This makes sets a good choice when the main requirement is:

- membership checking
- uniqueness
- duplicate detection

### Choosing the data structure

The first implementation effectively performs:

```text
for each event
    scan the events again
```

which leads to:

```text
O(n²)
```

The improved implementation performs:

```text
for each event
    hash lookup
```

which leads to:

```text
O(n)
```

The data structure therefore changes the scalability of the algorithm.

### Main takeaway

Choosing the correct data structure can improve both **performance** and **code simplicity**.

For this problem:

```text
list approach → O(n²)
set approach  → O(n)
```

The difference may appear small with a few records, but becomes significant as the dataset grows.

This is particularly relevant in Data Engineering, where the same algorithm may need to process millions of records.

---

## Next

The next step is to study dictionaries as hash maps and use them to solve an aggregation problem.

Topics:

- `dict`
- Key/value storage
- Hash-based lookup
- Aggregation by key
- `dict.get()`
- Time and space complexity

Next exercise:

```text
Aggregate transaction amounts by user_id.
```
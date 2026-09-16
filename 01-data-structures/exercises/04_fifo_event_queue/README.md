# Exercise 04 — FIFO Event Queue

## Goal

Implement an event queue using the **FIFO** principle:

```text
First In, First Out
```

The first event added to the queue is also the first event to be processed.

## Input

```python
events = [
    {"event_id": "e1", "type": "created"},
    {"event_id": "e2", "type": "updated"},
    {"event_id": "e3", "type": "deleted"},
]
```

## Expected Output

```python
[
    {"event_id": "e1", "type": "created"},
    {"event_id": "e2", "type": "updated"},
    {"event_id": "e3", "type": "deleted"},
]
```

The output order must match the input order.

## V1 — Queue implemented with `list`

The first version uses a Python list.

```python
queue = events.copy()

while queue:
    event = queue.pop(0)
    processed_events.append(event)
```

`pop(0)` removes the first element from the list.

The issue is that, after removing an element, Python must shift all remaining elements one position to the left.

For this reason, each `pop(0)` operation takes `O(n)` time in the worst case.

Processing all events results in:

```text
O(n²)
```

## V2 — Queue implemented with `deque`

The second version uses `deque` from `collections`.

```python
from collections import deque
```

```python
queue = deque(events)

while queue:
    event = queue.popleft()
    processed_events.append(event)
```

`popleft()` removes the first element from the queue without shifting the remaining elements.

Each removal takes:

```text
O(1)
```

Processing `n` events therefore takes:

```text
O(n)
```

## Complexity

| Version                  | Remove first element | Total time |  Space |
| ------------------------ | -------------------: | ---------: | -----: |
| `list` with `pop(0)`     |               `O(n)` |    `O(n²)` | `O(n)` |
| `deque` with `popleft()` |               `O(1)` |     `O(n)` | `O(n)` |

Both versions create a separate queue and do not modify the input list.

## Benchmark

The two implementations were compared using `time.perf_counter()` and the average of five runs.

| Events |  List `pop(0)` | `deque.popleft()` |
| -----: | -------------: | ----------------: |
|     10 | 0.0000017760 s |    0.0000019016 s |
|    100 | 0.0000279202 s |    0.0000202110 s |
|  1,000 | 0.0001163052 s |    0.0000480954 s |
| 10,000 | 0.0062832778 s |    0.0005421280 s |

With 10,000 events, `deque` is approximately **11.6 times faster** than the list implementation.

When increasing the input size from 1,000 to 10,000 events:

* the list implementation goes from `0.000116` to `0.006283` seconds, approximately **54 times slower**;
* `deque` goes from `0.000048` to `0.000542` seconds, approximately **11 times slower**.

This behavior is consistent with the expected complexities:

```text
list pop(0)       → O(n²)
deque popleft()   → O(n)
```

## Tests

The tests verify that both implementations:

* process events in FIFO order;
* return an empty list for an empty queue;
* do not modify the input list.

## What I Learned

A list can represent a queue conceptually, but `pop(0)` becomes inefficient as the queue grows.

`collections.deque` is designed to efficiently add and remove elements from both ends.

For FIFO queues in Python, the preferred choice is usually:

```python
deque
```

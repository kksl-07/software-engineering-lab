# Exercise 06 — Priority Event Queue

## Goal

Implement an event queue that processes events according to their priority.

Unlike FIFO and LIFO structures, a priority queue does not process events based only on insertion order.

```text
FIFO     → first event added is processed first
LIFO     → last event added is processed first
Priority → highest-priority event is processed first
```

For this exercise, a lower numeric value means a higher priority:

```text
priority 1 → highest priority
priority 3 → lowest priority
```

## Input

```python
events = [
    {"event_id": "e1", "priority": 3, "type": "email"},
    {"event_id": "e2", "priority": 1, "type": "payment_failed"},
    {"event_id": "e3", "priority": 2, "type": "profile_updated"},
]
```

## Expected Output

```python
[
    {"event_id": "e2", "priority": 1, "type": "payment_failed"},
    {"event_id": "e3", "priority": 2, "type": "profile_updated"},
    {"event_id": "e1", "priority": 3, "type": "email"},
]
```

## Equal Priorities

When two events have the same priority, the implementation preserves their arrival order.

```python
events = [
    {"event_id": "e1", "priority": 1, "type": "payment_failed"},
    {"event_id": "e2", "priority": 1, "type": "payment_failed"},
    {"event_id": "e3", "priority": 2, "type": "email"},
]
```

Expected output:

```python
[
    {"event_id": "e1", "priority": 1, "type": "payment_failed"},
    {"event_id": "e2", "priority": 1, "type": "payment_failed"},
    {"event_id": "e3", "priority": 2, "type": "email"},
]
```

This is achieved with an insertion-order counter.

```python
(priority, insertion_order, event)
```

The heap compares priority first. If priorities are equal, it compares the insertion order.

## V1 — Priority Queue Implemented with `list`

The first version uses a normal list.

For every processed event, it scans the whole list to find the event with the lowest priority.

```python
event_index = min(
    range(len(queue)),
    key=lambda index: (queue[index]["priority"], index),
)

event = queue.pop(event_index)
```

Finding the minimum takes `O(n)` time. This happens once for every event.

Therefore, processing all events takes:

```text
O(n²)
```

## V2 — Priority Queue Implemented with `heapq`

The second version uses `heapq`, which implements a min-heap.

```python
heapq.heappush(
    priority_queue,
    (event["priority"], insertion_order, event),
)
```

```python
_, _, event = heapq.heappop(priority_queue)
```

A min-heap always keeps the smallest element available for efficient extraction.

## Complexity

| Operation                      | List implementation | `heapq` implementation |
| ------------------------------ | ------------------: | ---------------------: |
| Insert one event               |              `O(1)` |             `O(log n)` |
| Find and remove the next event |              `O(n)` |             `O(log n)` |
| Process `n` events             |             `O(n²)` |           `O(n log n)` |
| Space complexity               |              `O(n)` |                 `O(n)` |

## Benchmark

The benchmark compares the two implementations using repeated priorities from `1` to `5` and the average of three runs.

| Events |       List |    `heapq` | `heapq` speedup |
| -----: | ---------: | ---------: | --------------: |
|    100 | 0.000644 s | 0.000051 s |           12.6× |
|    500 | 0.017883 s | 0.000375 s |           47.7× |
|  1,000 | 0.069192 s | 0.000573 s |          120.8× |
|  2,000 | 0.276373 s | 0.001129 s |          244.8× |

When increasing the input size from 1,000 to 2,000 events:

```text
list  → approximately 4× slower
heapq → approximately 2× slower
```

This matches the expected growth:

```text
list  → O(n²)
heapq → O(n log n)
```

## Tests

The tests verify that the implementation:

* processes events from highest to lowest priority;
* returns an empty list for an empty priority queue;
* does not modify the input list;
* preserves FIFO order when priorities are equal;
* raises `KeyError` when an event does not contain `priority`.

## When to Use `sorted()` Instead

If all events are already available and you only need to order them once, `sorted()` is often simpler:

```python
sorted(events, key=lambda event: event["priority"])
```

Sorting all events once has `O(n log n)` complexity.

A priority queue is more useful when events arrive progressively and the system repeatedly needs to retrieve the next most important event.

## What I Learned

A priority queue is useful when processing order depends on importance rather than arrival time.

`heapq` is an efficient choice for dynamic scheduling because it supports:

```text
insert next event  → O(log n)
extract next event → O(log n)
```

For production systems, priority queues are useful for scheduling urgent jobs, processing critical failures, handling retries, and prioritizing workloads with different SLAs.

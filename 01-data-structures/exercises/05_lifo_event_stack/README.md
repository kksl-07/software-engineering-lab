# Exercise 05 — LIFO Event Stack

## Goal

Implement an event stack using the **LIFO** principle:

```text
Last In, First Out
```

The last event added to the stack is the first event to be processed.

A stack is useful when the most recent operation must be handled first, for example in undo functionality.

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
    {"event_id": "e3", "type": "deleted"},
    {"event_id": "e2", "type": "updated"},
    {"event_id": "e1", "type": "created"},
]
```

The output order is the reverse of the input order.

## Implementation with `list`

A Python `list` is suitable for implementing a stack.

```python
stack = events.copy()

while stack:
    event = stack.pop()
    processed_events.append(event)
```

The copied list is used as the stack, so the original input list is not modified.

`pop()` removes and returns the last element in the list. This corresponds to removing the element at the top of the stack.

## Complexity

| Operation                            | Average time complexity |
| ------------------------------------ | ----------------------: |
| Add an event with `append()`         |                  `O(1)` |
| Remove the latest event with `pop()` |                  `O(1)` |
| Process `n` events                   |                  `O(n)` |
| Space complexity                     |                  `O(n)` |

Unlike `pop(0)`, `pop()` does not need to shift the remaining elements in the list.

```text
list.pop(0)  → removes from the beginning → O(n)
list.pop()   → removes from the end       → O(1)
```

For this reason, a Python list is an efficient and simple choice for LIFO stacks.

## Tests

The tests verify that the implementation:

* processes events in LIFO order;
* returns an empty list for an empty stack;
* does not modify the input list.

## What I Learned

A stack and a queue may contain the same elements, but they process them in different orders:

```text
Queue → FIFO → First In, First Out
Stack → LIFO → Last In, First Out
```

For a LIFO stack in Python, `list.append()` and `list.pop()` provide an efficient implementation.

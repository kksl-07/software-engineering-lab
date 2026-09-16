from collections import deque


def process_events_with_list(events: list[dict[str, str]]) -> list[dict[str, str]]:
    queue = events.copy()
    processed_events = []

    while queue:
        event = queue.pop(0)
        processed_events.append(event)

    return processed_events

def process_events_with_deque(events: list[dict[str, str]],) -> list[dict[str, str]]:
    queue = deque(events)
    processed_events = []

    while queue:
        event = queue.popleft()
        processed_events.append(event)
    return processed_events

def main():
    events = [
        {"event_id": "e1", "type": "created"},
        {"event_id": "e2", "type": "updated"},
        {"event_id": "e3", "type": "deleted"},
    ]
    out_q = process_events_with_deque(events)
    return out_q

if __name__ == "__main__":
    q = main()
    print(q)


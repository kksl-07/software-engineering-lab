import heapq

def process_events_by_priority(
    events: list[dict[str, int | str]],
) -> list[dict[str, int | str]]:
    priority_queue = []
    processed_events = []

    for insertion_order, event in enumerate(events):
        heapq.heappush(priority_queue, (event["priority"], insertion_order, event))

    while priority_queue:
        _, _, event = heapq.heappop(priority_queue)
        processed_events.append(event)

    return processed_events

def process_events_by_priority_with_list(
    events: list[dict[str, int | str]],
) -> list[dict[str, int | str]]:
    queue = events.copy()
    processed_events = []

    while queue:
        event_index = min(
            range(len(queue)),
            key=lambda index: (queue[index]["priority"], index),
        )

        event = queue.pop(event_index)
        processed_events.append(event)

    return processed_events

def main():
    events = [
        {"event_id": "e1", "priority": 3, "type": "email"},
        {"event_id": "e2", "priority": 1, "type": "payment_failed"},
        {"event_id": "e3", "priority": 1, "type": "profile_updated"},
    ]
    return process_events_by_priority_with_list(events)

if __name__ == "__main__":
    print(main())
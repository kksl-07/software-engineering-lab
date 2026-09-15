def process_events_with_stack(
    events: list[dict[str, str]],
) -> list[dict[str, str]]:
    stack = events.copy()
    processed_events = []

    while stack:
        event = stack.pop(-1)
        processed_events.append(event)

    return processed_events

def main():
    events = [
        {"event_id": "e1", "type": "created"},
        {"event_id": "e2", "type": "updated"},
        {"event_id": "e3", "type": "deleted"},
    ]
    print(process_events_with_stack(events))

if __name__ == "__main__":
    main()

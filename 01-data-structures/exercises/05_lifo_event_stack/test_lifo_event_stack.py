from lifo_event_stack import process_events_with_stack

def test_processes_events_in_lifo_order():
    events = [
        {"event_id": "e1", "type": "created"},
        {"event_id": "e2", "type": "updated"},
        {"event_id": "e3", "type": "deleted"},
    ]
    processed_events = process_events_with_stack(events)
    assert processed_events == [{'event_id': 'e3', 'type': 'deleted'}, {'event_id': 'e2', 'type': 'updated'}, {'event_id': 'e1', 'type': 'created'}]

def test_returns_empty_list_for_empty_stack():
    events = []
    processed_events = process_events_with_stack(events)

    assert processed_events == []

def test_does_not_modify_input_events():

    events = []
    original_events = events.copy()

    process_events_with_stack(events)

    assert events == original_events
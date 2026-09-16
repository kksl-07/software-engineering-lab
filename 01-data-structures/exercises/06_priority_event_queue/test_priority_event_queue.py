import pytest

from priority_event_queue import process_events_by_priority

def test_processes_events_from_highest_to_lowest_priority():
    events = [
        {"event_id": "e1", "priority": 3, "type": "email"},
        {"event_id": "e2", "priority": 1, "type": "payment_failed"},
        {"event_id": "e3", "priority": 2, "type": "profile_updated"},
    ]

    processed_events = process_events_by_priority(events)
    assert processed_events == [{'event_id': 'e2', 'priority': 1, 'type': 'payment_failed'}, {'event_id': 'e3', 'priority': 2, 'type': 'profile_updated'}, {'event_id': 'e1', 'priority': 3, 'type': 'email'}]

def test_returns_empty_list_for_empty_priority_queue():
    events = []
    processed_events = process_events_by_priority(events)
    assert processed_events == []

def test_does_not_modify_input_events():
    events = [
        {"event_id": "e1", "priority": 3, "type": "email"},
        {"event_id": "e2", "priority": 1, "type": "payment_failed"},
        {"event_id": "e3", "priority": 2, "type": "profile_updated"},
    ]
    original_events = events.copy()
    process_events_by_priority(events)
    assert events == original_events

def test_keeps_fifo_order_when_priorities_are_equal():
    events = [
        {"event_id": "e1", "priority": 3, "type": "email"},
        {"event_id": "e2", "priority": 1, "type": "payment_failed"},
        {"event_id": "e3", "priority": 1, "type": "profile_updated"},
    ]
    processed_events = process_events_by_priority(events)
    assert processed_events == [{'event_id': 'e2', 'priority': 1, 'type': 'payment_failed'}, {'event_id': 'e3', 'priority': 1, 'type': 'profile_updated'}, {'event_id': 'e1', 'priority': 3, 'type': 'email'}]

def test_raises_key_error_when_priority_is_missing():
    events = [
        {"event_id": "e1", "type": "email"},
        {"event_id": "e2", "priority": 1, "type": "payment_failed"},
        {"event_id": "e3", "priority": 1, "type": "profile_updated"},
    ]

    with pytest.raises(KeyError) as e:
        process_events_by_priority(events)

    assert e.value.args[0] == "priority"
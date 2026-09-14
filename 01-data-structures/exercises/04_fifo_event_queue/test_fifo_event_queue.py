from fifo_event_queue import process_events_with_list

def test_processes_events_in_fifo_order():
    events = [
        {"event_id": "e1", "type": "created"},
        {"event_id": "e2", "type": "updated"},
        {"event_id": "e3", "type": "deleted"},
    ]
    processed_events = process_events_with_list(events)
    assert processed_events == [{'event_id': 'e1', 'type': 'created'},
                                {'event_id': 'e2', 'type': 'updated'},
                                {'event_id': 'e3', 'type': 'deleted'}]

def test_returns_empty_list_for_empty_queue():
    events = []
    processed_events = process_events_with_list(events)
    assert processed_events == []

def test_does_not_modify_input_events():
    events = [{'event_id': 'e1', 'type': 'created'},
              {'event_id': 'e2', 'type': 'updated'},
              {'event_id': 'e3', 'type': 'deleted'}
              ]
    original_events = events.copy()
    process_events_with_list(events)
    assert original_events == events
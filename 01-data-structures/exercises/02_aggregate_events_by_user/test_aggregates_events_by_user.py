import pytest

from aggregate_events_by_user import aggregate_events_by_user_v1


def test_aggregate_events_by_user():
    events = [
        {"user_id": "u1", "duration": 10},
        {"user_id": "u2", "duration": 5},
        {"user_id": "u1", "duration": 7},
        {"user_id": "u3", "duration": 4},
        {"user_id": "u2", "duration": 8}
    ]
    res = aggregate_events_by_user_v1(events)
    assert res == {"u1":17, "u2": 13, "u3": 4}

def test_returns_empty_dict_for_empty_events():
    events = []
    res = aggregate_events_by_user_v1(events)
    assert res == {}

def test_raises_key_error_when_user_id_is_missing():
    events = [
        {"duration": 10},
    ]

    with pytest.raises(KeyError) as error:
        aggregate_events_by_user_v1(events)

    assert error.value.args[0] == "user_id"

def test_raises_key_error_when_duration_is_missing():
    events = [
        {"user_id": "u1"},
    ]

    with pytest.raises(KeyError) as error:
        aggregate_events_by_user_v1(events)

    assert error.value.args[0] == "duration"

def test_raises_key_error_when_both_fields_are_missing():
    events = [
        {},
    ]

    with pytest.raises(KeyError) as error:
        aggregate_events_by_user_v1(events)

    assert error.value.args[0] == "user_id"
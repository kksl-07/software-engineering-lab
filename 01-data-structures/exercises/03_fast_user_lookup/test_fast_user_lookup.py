import pytest

from fast_user_lookup import find_user_by_id_v1

def test_returns_user_when_present_at_beginning():

    users = [
        {"user_id": "u1", "name": "Alice"},
        {"user_id": "u2", "name": "Bob"},
        {"user_id": "u3", "name": "Charlie"},
    ]
    target_user_id = "u1"

    assert find_user_by_id_v1(users, target_user_id) == {'user_id': 'u1', 'name': 'Alice'}

def test_returns_user_when_present_in_middle():
    users = [
        {"user_id": "u1", "name": "Alice"},
        {"user_id": "u2", "name": "Bob"},
        {"user_id": "u3", "name": "Charlie"},
    ]

    target_user_id = "u2"
    assert find_user_by_id_v1(users, target_user_id) == {"user_id": "u2", "name": "Bob"}

def test_returns_user_when_present_at_end():

    users = [
        {"user_id": "u1", "name": "Alice"},
        {"user_id": "u2", "name": "Bob"},
        {"user_id": "u3", "name": "Charlie"},
    ]

    target_user_id = "u3"
    assert find_user_by_id_v1(users, target_user_id) == {"user_id": "u3", "name": "Charlie"}

def test_returns_none_when_user_does_not_exist():
    users = [
        {"user_id": "u1", "name": "Alice"},
        {"user_id": "u2", "name": "Bob"},
    ]

    target_user_id = "u99"
    assert find_user_by_id_v1(users, target_user_id) is None

def test_returns_none_when_users_list_is_empty():

    users = []
    target_user_id = "u1"

    assert find_user_by_id_v1(users, target_user_id) is None

def test_raises_key_error_when_user_id_is_missing():

    users = [
        {"name": "Alice"},
    ]

    target_user_id = "u1"
    with pytest.raises(KeyError) as e:
        find_user_by_id_v1(users, target_user_id)

    assert e.value.args[0] == "user_id"
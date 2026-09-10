from collections import defaultdict

def aggregate_events_by_user_v1(events: list[dict[str, int | str]]) -> dict[str, int]:
    total_duration_by_user = {}

    for event in events:
        user_id = event["user_id"]
        duration = event["duration"]

        if user_id not in total_duration_by_user:
            total_duration_by_user[user_id] = 0

        total_duration_by_user[user_id] += duration

    return total_duration_by_user

def aggregate_events_by_user_v2(events: list[dict[str, int | str]]) -> dict[str, int]:
    total_duration_by_user = {}

    for event in events:
        user_id = event["user_id"]
        duration = event["duration"]
        total_duration_by_user[user_id] = (
                total_duration_by_user.get(user_id, 0) + duration
        )

    return total_duration_by_user

def aggregate_events_by_user_v3( events: list[dict[str, int | str]],) -> dict[str, int]:
    total_duration_by_user = defaultdict(int)

    for event in events:
        user_id = event["user_id"]
        duration = event["duration"]

        total_duration_by_user[user_id] += duration

    return dict(total_duration_by_user)

def main():
    events = [
        {"user_id": "u1", "duration": 10},
        {"user_id": "u2", "duration": 5},
        {"user_id": "u1", "duration": 7},
        {"user_id": "u3", "duration": 4},
        {"user_id": "u2", "duration": 8},
    ]
    print(aggregate_events_by_user_v1(events))


if __name__ == "__main__":
    main()
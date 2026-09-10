"""
Exercise 01 - Find duplicate events

Given a collection of events, return the event IDs that occur
more than once.

Constraints:
- Do NOT use set.
- Do NOT use dict.
- Use only lists and loops.

Expected result:
["e1", "e2"]
"""
import random
import time


def generate_events(n: int) -> list[dict]:
    return [
        {
            "event_id": f"e{random.randint(1, n // 2)}"
        }
        for _ in range(n)
    ]

def find_duplicates_v1(events: list[dict]) -> list:
    event_ids_list = []
    dupes = []
    for event in events:
        event_ids_list.append(event["event_id"])
    duplicates = [i for i in event_ids_list if event_ids_list.count(i) > 1]
    for e in duplicates:
        if e not in dupes:
            dupes.append(e)

    return dupes


def find_duplicates_v2(events: list[dict]) -> list[str]:
    seen = set()
    duplicates = set()

    for event in events:
        event_id = event["event_id"]
        if event_id not in seen:
            seen.add(event_id)
        else:
            duplicates.add(event_id)

    return list(duplicates)


def main() -> None:
    for size in [1_000, 5_000, 10_000, 20_000]:
        events = generate_events(size)

        start = time.perf_counter()
        find_duplicates_v1(events)
        v1_time = time.perf_counter() - start

        start = time.perf_counter()
        find_duplicates_v2(events)
        v3_time = time.perf_counter() - start

        print(
            f"{size:>6} events | "
            f"V1: {v1_time:.6f}s | "
            f"V3: {v3_time:.6f}s"
        )


if __name__ == "__main__":
    main()
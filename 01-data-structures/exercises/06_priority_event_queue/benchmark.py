import time

from priority_event_queue import (
    process_events_by_priority,
    process_events_by_priority_with_list,
)


def generate_events(number_of_events: int) -> list[dict[str, int | str]]:
    return [
        {
            "event_id": f"e{index}",
            "priority": (index % 5) + 1,
            "type": "event",
        }
        for index in range(number_of_events)
    ]


def measure_average_time(function, events, repetitions: int) -> float:
    start = time.perf_counter()

    for _ in range(repetitions):
        function(events)

    return (time.perf_counter() - start) / repetitions


def main() -> None:
    sizes = [100, 500, 1_000, 2_000]
    repetitions = 3

    for size in sizes:
        events = generate_events(size)

        list_time = measure_average_time(
            process_events_by_priority_with_list,
            events,
            repetitions,
        )

        heap_time = measure_average_time(
            process_events_by_priority,
            events,
            repetitions,
        )

        print(
            f"{size:>6,} events | "
            f"list: {list_time:.6f}s | "
            f"heapq: {heap_time:.6f}s"
        )


if __name__ == "__main__":
    main()
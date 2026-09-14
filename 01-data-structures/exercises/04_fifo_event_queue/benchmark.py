from fifo_event_queue import (process_events_with_list,
                              process_events_with_deque
                              )
import time

def generate_events(number_of_events: int) -> list[dict[str, str]]:
    return [
        {
            "event_id": f"e{index}",
            "type": "created",
        }
        for index in range(number_of_events)
    ]

def main() -> None:
    sizes = [10, 100, 1_000, 10_000]
    repetitions = 5

    for size in sizes:
        events = generate_events(size)

        start = time.perf_counter()

        for _ in range(repetitions):
            process_events_with_list(events)
        list_end_time = (time.perf_counter() - start) / repetitions

        start = time.perf_counter()

        for _ in range(repetitions):
            process_events_with_deque(events)
        queue_end_time = (time.perf_counter() - start) / repetitions


        print(
            f"{size:>6} eventi | "
            f"lista pop(0): {list_end_time:.10f}s | "
            f"deque popleft(): {queue_end_time:.10f}s"
        )

if __name__ == "__main__":
    main()
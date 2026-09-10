import time

from fast_user_lookup import (
    build_user_index,
    find_user_by_id_v1,
    find_user_by_id_v2,
)


def generate_users(number_of_users: int) -> list[dict[str, str]]:
    return [
        {
            "user_id": f"u{index}",
            "name": f"User {index}",
        }
        for index in range(number_of_users)
    ]


def main() -> None:
    sizes = [10, 100, 1_000, 10_000, 100_000]
    repetitions = 1_000

    for size in sizes:
        users = generate_users(size)
        target_user_id = f"u{size - 1}"

        start = time.perf_counter()
        user_index = build_user_index(users)
        index_build_time = time.perf_counter() - start

        start = time.perf_counter()

        for _ in range(repetitions):
            find_user_by_id_v1(users, target_user_id)

        v1_average_time = (time.perf_counter() - start) / repetitions

        start = time.perf_counter()

        for _ in range(repetitions):
            find_user_by_id_v2(user_index, target_user_id)

        v2_average_time = (time.perf_counter() - start) / repetitions

        print(
            f"{size:>6} utenti | "
            f"creazione indice: {index_build_time:.8f}s | "
            f"ricerca lista: {v1_average_time:.10f}s | "
            f"ricerca dizionario: {v2_average_time:.10f}s"
        )


if __name__ == "__main__":
    main()
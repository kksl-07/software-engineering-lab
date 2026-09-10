
def build_user_index(users: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    users_index = {}
    for user in users:
        users_index[user["user_id"]] = user

    return users_index


def find_user_by_id_v1(users: list[dict[str, str]], target_user_id: str,) -> dict[str, str] | None:

    for user in users:
        if user["user_id"] == target_user_id:
            return user
    return None


def find_user_by_id_v2(users: dict[str, dict[str,str]], target_user_id: str) -> dict[str, str] | None:
    return users.get(target_user_id)

def main():
    users = [
        {"user_id": "u1", "name": "Alice"},
        {"user_id": "u2", "name": "Bob"},
        {"user_id": "u3", "name": "Charlie"},
    ]
    user_to_find = "u3"
    users_index = build_user_index(users)
    print(find_user_by_id_v2(users_index, user_to_find))


if __name__ == "__main__":
    main()
import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    initial_names = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]
    print(f"\nInitial list of players: {initial_names}")

    capitalized_names = [name.capitalize() for name in initial_names]
    print(f"\nNew list with all names capitalized: {capitalized_names}")

    capitalized_only = [name for name in initial_names if name[0].isupper()]
    print(f"\nNew list of capitalized names only: {capitalized_only}")

    scores = {name: random.randint(0, 1000) for name in capitalized_names}
    print(f"\nScore dict: {scores}")

    avg = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg}")

    high_scores = {name: s for name, s in scores.items() if s > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()

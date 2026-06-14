import random


def generate_random(achievements: list[str]) -> set[str]:
    num = random.randint(3, 9)
    return set(random.sample(achievements, num))


def main() -> None:
    achievements = [
        "Go Outside",
        "Welcome to the Achievement",
        "Unachievable",
        "Speed Run",
        "The Broom Closet",
        "Test Achievement Please Ignore",
        "This Achievement Is a Lie",
        "Confusion",
        "The End Is Never",
        "Infinite Loop",
        "Existential Crisis",
        "That's Not How You're Supposed to Play",
        "Bread",
        "Touch Grass",
        "Serious Achievement",
        "Unserious Achievement",
    ]

    players = ["Alice", "Bob", "Charlie", "Dylan"]
    player_sets = {name: generate_random(achievements) for name in players}

    print("=== Achievement Tracker System ===\n")

    for name, ach_set in player_sets.items():
        print(f"Player {name}: {ach_set}")

    all_distinct: set[str] = set()
    for s in player_sets.values():
        all_distinct = all_distinct.union(s)
    print(f"\nAll distinct achievements: {all_distinct}")

    common = set(achievements)
    for s in player_sets.values():
        common = common.intersection(s)
    print(f"\nCommon achievements: {common}")

    for name, s in player_sets.items():
        unique = s.copy()
        for other_name, other_set in player_sets.items():
            if other_name != name:
                unique = unique.difference(other_set)
        print(f"\nOnly {name} has: {unique}")

    for name, s in player_sets.items():
        missing = set(achievements).difference(s)
        print(f"\n{name} is missing: {missing}")


if __name__ == "__main__":
    main()

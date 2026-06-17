import typing
import random


# infinite generator that yields random (player, action) events
def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan", "eve"]
    actions = ["run", "eat", "move", "grab", "use", "swim", "jump"]
    while True:
        yield (random.choice(players), random.choice(actions))


# pick a random index from the event list, pop and yield.
# stops when the list is empty.
def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        yield events.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()
    for i in range(1000):
        name, action = next(event_generator)
        print(f"Event {i}: Player {name} "
              f"did action {action}")

    ten_events = [next(gen_event()) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()

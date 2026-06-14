import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coords = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = coords.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        values = []
        valid = True
        for part in parts:
            try:
                values.append(float(part.strip()))
            except ValueError as e:
                print(f"Error on parameter '{part.strip()}': {e}")
                valid = False
                break
        if valid:
            return (values[0], values[1], values[2])


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    dist_center = math.sqrt(pos1[0] ** 2 + pos1[1] ** 2 + pos1[2] ** 2)
    result1 = round(dist_center, 4)
    print(f"Distance to center: {result1}")
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    dist_between = round(math.sqrt(
        (pos2[0] - pos1[0]) ** 2
        + (pos2[1] - pos1[1]) ** 2
        + (pos2[2] - pos1[2]) ** 2
    ), 4)
    print(f"Distance between the 2 sets of coordinates: {dist_between}")


if __name__ == "__main__":
    main()

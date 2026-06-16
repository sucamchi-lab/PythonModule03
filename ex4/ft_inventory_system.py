import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = {}
    params = sys.argv[1:]

    for param in params:
        if ':' not in param or param.count(':') != 1:
            print(f"Error - invalid parameter '{param}'")
            continue

        item_name, quantity_str = param.split(':', 1)

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
        except ValueError:
            print(f"Quantity error for '{item_name}': invalid literal for int() with base 10: '{quantity_str}'")
            continue

        inventory[item_name] = quantity

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    if inventory:
        for item, qty in inventory.items():
            percent = round((qty / total_qty) * 100, 1)
            print(f"Item {item} represents {percent}%")

        most_abundant = max(inventory, key=lambda k: inventory[k])
        least_abundant = min(inventory, key=lambda k: inventory[k])
        print(f"Item most abundant: {most_abundant} with quantity {inventory[most_abundant]}")
        print(f"Item least abundant: {least_abundant} with quantity {inventory[least_abundant]}")

    inventory.update({'Magical Staff of Poopy-Farts': 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()

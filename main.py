print("WARESYNC\n")
# Dictionary
inventory = {
    'Food': [],
    'Household Items': [],
    'Others': []
}

categories = list(inventory.keys())


# Entry of Item
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Quantity must be positive.")
        except ValueError:
            print("Invalid quantity.")


while True:
    action = input("Add, remove, show, or end? ").strip().lower()
    # Terminate the system
    if action == 'end':
        print("Exiting system.")
        break

    elif action == 'add':
        print("\nCategories:")
        for i, cat in enumerate(categories, 1):
            print(str(i) + ".", cat)

        choice = input("Choose 1-3: ").strip()
        if choice not in {'1', '2', '3'}:
            print("Invalid choice.")
            continue

        category = categories[int(choice) - 1]
        name = input("Product name: ").strip()
        quantity = get_positive_integer("Quantity: ")
        expiration = input("Expiration (dd/mm/yy): ").strip()

        inventory[category].append({
            'name': name,
            'quantity': quantity,
            'expiration': expiration
        })
        print("Added", name, "to", category)

    elif action == 'remove':
        print("\nCategories:")
        for i, cat in enumerate(categories, 1):
            print(str(i) + ".", cat)

        choice = input("Choose 1-3: ").strip()
        if choice not in {'1', '2', '3'}:
            print("Invalid choice.")
            continue

        category = categories[int(choice) - 1]
        name = input("Product name: ").strip().lower()
        remove_quantity = get_positive_integer("Quantity to remove: ")
        expiration = input("Expiration (dd/mm/yy): ").strip()

        found = False
        for item in inventory[category]:
            if (item['name'].lower() == name and
                    item['expiration'] == expiration):
                if remove_quantity >= item['quantity']:
                    inventory[category].remove(item)
                    print("Removed all", item['quantity'], "of", name)
                else:
                    item['quantity'] -= remove_quantity
                    print("Removed", remove_quantity, "from", name)
                    print(name, "now has", item['quantity'], "remaining")
                found = True
                break
        if not found:
            print("Product not found")

    elif action == 'show':
        empty = True
        for category, items in inventory.items():
            if items:
                empty = False
                print("\n" + category + ":")
                for item in items:
                    print(item['name'], item['quantity'], "Exp:", item['expiration'])
        if empty:
            print("\nInventory empty")

    else:
        print("Invalid action. Try again.")

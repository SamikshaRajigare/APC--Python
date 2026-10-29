inventory = {}
def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))

    inventory[name] = quantity
    print("Product added successfully.")
def update_product():
    name = input("Enter product name: ")

    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name] = quantity
        print("Quantity updated.")
    else:
        print("Product not found.")
def remove_product():
    name = input("Enter product name: ")

    if name in inventory:
        if inventory[name] == 0:
            del inventory[name]
            print("Product removed.")
        else:
            print("Product still has stock.")
    else:
        print("Product not found.")
def analyze_inventory():
    print("\nInventory:", inventory)

    if len(inventory) > 0:
        highest = max(inventory, key=inventory.get)
        print("Product with highest stock:", highest)
        print("Highest quantity:", inventory[highest])

    print("Total unique products:", len(inventory))
while True:
    print("\n1. Add Product")
    print("2. Update Product")
    print("3. Remove Product")
    print("4. Analyze Inventory")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_product()

    elif choice == 2:
        update_product()

    elif choice == 3:
        remove_product()

    elif choice == 4:
        analyze_inventory()

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

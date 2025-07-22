def display_menu():
    print("Shopping List Manager")

shopping_list = []

while True:
    print("\nMenu:")
    print("1. Add item")
    print("2. View items")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} added to the shopping list.")

    elif choice == '2':
        print("Your Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


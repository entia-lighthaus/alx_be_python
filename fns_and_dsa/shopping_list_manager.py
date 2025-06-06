def main():
    shopping_list = []

    while True:
        print("\nShopping List Manager")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View shopping list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"{item} added to shopping list.")

        elif choice == "2":
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from shopping list.")
            else:
                print(f"{item} not found in the shopping list.")

        elif choice == "3":
            if shopping_list:
                print("\nYour shopping list:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == "4":
            print("Exiting Shopping List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()

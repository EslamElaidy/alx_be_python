def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("enter the item to add")
            # Prompt for and add an item
            shopping_list.append(item)
            print(f"{item} has been add")
            
        elif choice == '2':
            item = input("enter the item to remove")
            shopping_list.remove(item)
            # Prompt for and remove an item
            
        elif choice == '3':
            # Display the shopping list
            print(f{shopping_list}
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



# shopping_list = []

# # Function to add an item to the shopping list
# def add_item(item):
#     shopping_list.append(item)  # Add the item to the list using append
#     print(f"'{item}' has been added to your shopping list.")  # Confirmation message

# # Function to remove an item from the shopping list
# def remove_item(item):
#     if item in shopping_list:  # Check if the item exists in the list
#         shopping_list.remove(item)  # Remove the item from the list
#         print(f"'{item}' has been removed from your shopping list.")  # Confirmation message
#     else:
#         print(f"'{item}' is not in your shopping list.")  # If item is not found, print this message

# # Function to display all items in the shopping list
# def display_list():
#     if shopping_list:  # Check if the shopping list is not empty
#         print("Your shopping list contains:")
#         for item in shopping_list:  # Loop through all the items in the list
#             print(f"- {item}")  # Print each item in the list
#     else:
#         print("Your shopping list is empty.")  # If the list is empty, print this message

# # Main function to interact with the user
# def main():
#     while True:  # Start an infinite loop to continuously interact with the user
#         print("\nShopping List Manager")  # Print the title of the menu
#         print("1. Add item to the list")
#         print("2. Remove item from the list")
#         print("3. Display shopping list")
#         print("4. Exit")  # Provide options to the user
        
#         choice = input("Enter your choice (1-4): ").strip()  # Get the user's choice and strip extra spaces
        
#         if choice == '1':  # If user chooses to add an item
#             item = input("Enter the item to add: ").strip()  # Get the item from the user
#             add_item(item)  # Call the add_item function to add the item to the list
        
#         elif choice == '2':  # If user chooses to remove an item
#             item = input("Enter the item to remove: ").strip()  # Get the item to remove
#             remove_item(item)  # Call the remove_item function to remove the item
        
#         elif choice == '3':  # If user chooses to display the list
#             display_list()  # Call the display_list function to show the current shopping list
        
#         elif choice == '4':  # If user chooses to exit
#             print("Goodbye! Exiting the program.")  # Print a goodbye message
#             break  # Break the loop to exit the program
        
#         else:  # If the user enters an invalid choice
#             print("Invalid choice. Please select a valid option.")  # Inform the user that the input was invalid

# if __name__ == "__main__":
#     main() 


# # Create a Python script named shopping_list_manager.py that implements a simple interface for managing a shopping list. This task focuses on using lists to store and manipulate data dynamically.


    
# def display_menu():
#     print("Shopping List Manager")
#     print("1. Add Item")
#     print("2. Remove Item")
#     print("3. View List")
#     print("4. Exit")

# def main():
#     shopping_list = []
#     while True:
#         display_menu()
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             item = input("Enter the item to add: ").strip()
#             if item:
#                 shopping_list.append(item)
#                 print(f'"{item}" has been added to your shopping list.')
#             else:
#                 print("Invalid input. Item cannot be empty.")
#             # Prompt for and add an item
#         elif choice == '2':
#             item = input("Enter the item to remove: ").strip()
#             if item in shopping_list:
#                 shopping_list.remove(item)
#                 print(f'"{item}" has been removed from your shopping list.')
#             else:
#                 print(f'"{item}" is not in the shopping list.')

#         elif choice == '3':
#             # Display the shopping list
#             if shopping_list:
#                 print("\nYour Shopping List:")
#                 for i, item in enumerate(shopping_list, start=1):
#                     print(f"{i}. {item}")
#             else:
#                 print("Your shopping list is empty.")
            
#         elif choice == '4':
#                 print("Goodbye!")
#                 break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()



def display_menu():
    """Display the menu options for the shopping list manager."""
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Exit")
    
def add_item(shopping_list):
    """Add an item to the shopping list."""
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f'"{item}" has been added to your shopping list.')
    else:
        print("Invalid input. Item cannot be empty.")


def remove_item(shopping_list):
    """Remove an item from the shopping list."""
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'"{item}" has been removed from your shopping list.')
    else:
        print(f'"{item}" is not in the shopping list.')


def view_list(shopping_list):
    """Display the current shopping list."""
    if shopping_list:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")


def main():
    """Main function to run the shopping list manager."""
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
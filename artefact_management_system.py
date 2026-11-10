
# Artefact Management System
# Local Heritage Community (LHC)

# Store artefact records
artefacts = {}


# Function 1: Display the main menu
def display_menu():
    print("\n===== ARTEFACT MANAGEMENT SYSTEM =====")
    print("1. Add Artefact")
    print("2. Update Artefact Condition")
    print("3. View All Artefacts")
    print("4. Search Artefact")
    print("5. Exit")


# Function 2: Get and validate menu choice
def get_menu_choice():
    while True:
        choice = input("Enter your choice (1-5): ")

        try:
            choice = int(choice)
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Function 3: Add a new artefact
def add_artefact():
    print("\n--- Add New Artefact ---")

    name = get_non_empty_input("Enter artefact name: ")

    if find_artefact(name) is not None:
        print("This artefact already exists.")
        return

    category = get_non_empty_input("Enter category: ")
    location = get_non_empty_input("Enter display location: ")
    condition = get_valid_condition()

    artefacts[name] = {
        "category": category,
        "location": location,
        "condition": condition
    }

    print("Artefact added successfully.")


# Function 4: Update an artefact's condition
def update_condition():
    print("\n--- Update Artefact Condition ---")

    name = get_non_empty_input("Enter artefact name: ")
    existing_name = find_artefact(name)

    if existing_name is None:
        print("Artefact not found.")
        return

    print("Current condition:", artefacts[existing_name]["condition"])
    new_condition = get_valid_condition()

    artefacts[existing_name]["condition"] = new_condition
    print("Artefact condition updated successfully.")


# Function 5: View all artefacts
def view_artefacts():
    print("\n--- All Artefacts ---")

    if not artefacts:
        print("No artefacts have been recorded yet.")
        return

    for name, details in artefacts.items():
        print("\nArtefact Name:", name)
        print("Category:", details["category"])
        print("Location:", details["location"])
        print("Condition:", details["condition"])


# Function 6: Search for an artefact
def search_artefact():
    print("\n--- Search Artefact ---")

    name = get_non_empty_input("Enter artefact name to search: ")
    existing_name = find_artefact(name)

    if existing_name is None:
        print("Artefact not found.")
    else:
        details = artefacts[existing_name]
        print("\nArtefact found!")
        print("Name:", existing_name)
        print("Category:", details["category"])
        print("Location:", details["location"])
        print("Condition:", details["condition"])


# Function 7: Prevent empty input
def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value
        else:
            print("This field cannot be left empty.")


# Function 8: Validate artefact condition
def get_valid_condition():
    valid_conditions = {
        "1": "Good",
        "2": "Damage",
        "3": "Under Repair"
    }

    while True:
        print("\nAvailable conditions:")
        print("1. Good")
        print("2. Damage")
        print("3. Under Repair")

        condition = input("Enter condition (1-3 or name): ").strip()

        if condition in valid_conditions:
            return valid_conditions[condition]

        for valid_condition in valid_conditions.values():
            if condition.lower() == valid_condition.lower():
                return valid_condition

        print("Invalid condition. Please select Good, Damage or Under Repair.")


# Function 9: Find an existing artefact
def find_artefact(name):
    for existing_name in artefacts:
        if existing_name.lower() == name.lower():
            return existing_name

    return None


# Function 10: Control the main program
def main():
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            add_artefact()
        elif choice == 2:
            update_condition()
        elif choice == 3:
            view_artefacts()
        elif choice == 4:
            search_artefact()
        elif choice == 5:
            print("Thank you for using the Artefact Management System.")
            break


# Start the program
if __name__ == "__main__":
    main()

phonebook = []

def add_contact(name, mobile=None, home=None, office=None, email=None):
    entry = {
        "name": name,
        "mobile": mobile,
        "home": home,
        "office": office,
        "email": email
    }
    phonebook.append(entry)
    print(f"Added contact: {name}")

def remove_contact(name):
    for entry in phonebook:
        if entry["name"].lower() == name.lower():
            phonebook.remove(entry)
            print(f"Removed contact: {name}")
            return
    print("Contact not found!")

def search_contact(keyword):
    results = [entry for entry in phonebook if keyword.lower() in entry["name"].lower()]
    if results:
        print("\n--- Search Results ---")
        for i, entry in enumerate(results, 1):
            print(f"{i}. {entry['name']} | Mobile: {entry['mobile']} | Home: {entry['home']} | Office: {entry['office']} | Email: {entry['email']}")
    else:
        print("No matching contacts found.")

def show_all_contacts():
    if not phonebook:
        print("Phone book is empty.")
    else:
        print("\n--- Contacts ---")
        for i, entry in enumerate(phonebook, 1):
            print(f"{i}. {entry['name']} | Mobile: {entry['mobile']} | Home: {entry['home']} | Office: {entry['office']} | Email: {entry['email']}")
        print(f"\nTotal contacts: {len(phonebook)}")

def main():
    while True:
        print("\n--- Phone Book Menu ---")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Show All Contacts")
        print("5. Exit")

        choice = input("Choose (1-5): ")

        if choice == "1":
            name = input("Enter name: ")
            mobile = input("Enter mobile number (or leave blank): ") or None
            home = input("Enter home number (or leave blank): ") or None
            office = input("Enter office number (or leave blank): ") or None
            email = input("Enter email (or leave blank): ") or None
            add_contact(name, mobile, home, office, email)

        elif choice == "2":
            name = input("Enter name to remove: ")
            remove_contact(name)

        elif choice == "3":
            keyword = input("Enter name keyword to search: ")
            search_contact(keyword)

        elif choice == "4":
            show_all_contacts()

        elif choice == "5":
            print("Closing phone book. Bye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

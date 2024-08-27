import json
import os


CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print(f"Contact {name} added successfully!")
    save_contacts(contacts)


def view_contacts(contacts):
    if contacts:
        print("\n--- Contact List ---")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("\nNo contacts available.")


def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").strip()
    if name in contacts:
        print(f"Editing contact: {name}")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
        email = input(f"Enter new email (current: {contacts[name]['email']}): ").strip()
        
        contacts[name]['phone'] = phone if phone else contacts[name]['phone']
        contacts[name]['email'] = email if email else contacts[name]['email']
        
        print(f"Contact {name} updated successfully!")
        save_contacts(contacts)
    else:
        print(f"Contact {name} not found!")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
        save_contacts(contacts)
    else:
        print(f"Contact {name} not found!")


def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("0. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "0":
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()

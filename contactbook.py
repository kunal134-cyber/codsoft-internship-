import pickle

def load_contacts():
    try:
        with open("contacts.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

# Save contacts to a file
def save_contacts(contacts):
    with open("contacts.pkl", "wb") as f:
        pickle.dump(contacts, f)

# Add a new contact
def add_contact(contacts):
    name = input("Enter the contact's name: ").strip()
    if name in contacts:
        print("This contact already exists!")
        return
    
    phone = input("Enter the phone number: ").strip()
    email = input("Enter the email: ").strip()
    address = input("Enter the address: ").strip()

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

# Search contacts by name or phone number
def search_contacts(contacts):
    search_term = input("Enter a name or phone number to search: ").strip()
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print(f"Found: {name} - Phone: {details['phone']} - Email: {details['email']} - Address: {details['address']}")
            found = True
    if not found:
        print("No contacts found matching your search.")

# Update a contact
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print(f"Contact '{name}' not found!")
        return
    
    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
    email = input(f"Enter new email (current: {contacts[name]['email']}): ").strip()
    address = input(f"Enter new address (current: {contacts[name]['address']}): ").strip()

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' updated successfully!")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found!")

# User interface
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()

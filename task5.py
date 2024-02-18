# contact book
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print(f"Contact {name} added successfully.")

    def view_contact_book(self):
        print("\nContact Book:")
        for name, contact_info in self.contacts.items():
            print(f"Name: {name}, Phone: {contact_info['Phone']}, Email: {contact_info['Email']}, Address: {contact_info['Address']}")

    def search_contact(self, keyword):
        results = []
        for name, contact_info in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in contact_info['Phone']:
                results.append((name, contact_info))
        return results

    def update_contact_book(self, name, new_phone, new_email, new_address):
        if name in self.contacts:
            contact = self.contacts[name]
            if new_phone:
                contact['Phone'] = new_phone
            if new_email:
                contact['Email'] = new_email
            if new_address:
                contact['Address'] = new_address
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

# Main function
def main():
    contact_book = ContactBook()

    while True:
        print("\n1. Add Contact\n2. View Contact List\n3. Search Contact\n4. Update Contact\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contact_book()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            search_results = contact_book.search_contact(keyword)
            print("\nSearch Results:")
            for name, contact_info in search_results:
                print(f"Name: {name}, Phone: {contact_info['Phone']}, Email: {contact_info['Email']}, Address: {contact_info['Address']}")

        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            new_phone = input("Enter new phone number (press Enter to keep existing): ")
            new_email = input("Enter new email address (press Enter to keep existing): ")
            new_address = input("Enter new address (press Enter to keep existing): ")
            contact_book.update_contact_book(name, new_phone, new_email, new_address)

        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

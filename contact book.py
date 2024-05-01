class Contact:
    def __init__(self, name , phone_number , email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        
    
class ContactBook:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self , contact):
        self.contacts.append(contact)
        print("Contact added successfully.")
    
    def view_contact(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for i, Contact in enumerate(self.contacts , start=1):
                print(f"{i}. Name: {Contact.name}, Phone: {Contact.phone_number}")
    
    def search_contact(self, search_query):
        search_results = []
        for contact in self.contacts:
            if search_query.lower() in contact.name.lower() or search_query in contact.phone_number:
                search_results.append(contact)
        if not search_results:
            print("No matching contacts found.")
        else:
            print("Search Results:")
            for i, contact in enumerate(search_results,start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")


    
    def update_contact(self, search_query,new_contact_info):
        search_results = []      
        for contact in self.contacts:
            if search_query.lower() in contact.name.lower() or search_query in contact.phone_number:
                search_results.append(contact)
        if not search_results:
            print("No matching contacts found.")
        else:
            for contact in search_results:
                contact.name = new_contact_info.get('name', contact.name)
                contact.phone_number = new_contact_info.get('Phone number',contact.phone_number)
                contact.phone_number = new_contact_info.get('Email',contact.email)
                contact.phone_number = new_contact_info.get('Address',contact.address)
                print("Contact updated successfully.")

    def delete_contact(self, search_query):
        search_results = []
        for contact in self.contacts:
            if search_query.lower()in contact.name.lower() or search_query in contact.phone_number:
                search_results.append(contact) 
            if not search_results:
                print("No matching contacts found.")
            else:
                for contact in search_results:
                    self.contacts.remove(contact)
                print("Contact deleted successfully.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n CONTACT BOOK MENU: ")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Seacrh Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")


        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Entr phone number: ")
            email = input("Enter email:")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
        elif choice == '2':
            contact_book.view_contact()
        elif choice == '3':
            search_query = input("Enter name or phone nu,ber to search: ")
            contact_book.search_contact(search_query)
        elif choice == '4':
            search_query = input("Enter name or Phone number to update: ")
            new_name = input("Enter new name (Press Enter to skip): ")
            new_phone_number = input("Enter phone number (Press Enter to skip): ") 
            new_email = input("Enter new email (Press Enter to skip): ") 
            new_address = input("Enter new address (Press Enter to skip): ")
            new_contact_info = {'name' : new_name , 'Phone_number' : new_phone_number,'email' : new_email,'address' : new_address}

            contact_book.update_contact(search_query, new_contact_info)  

        elif choice == '5':
            search_query = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_query)
        
        elif choice == '6':
            print("Exiting Contact Book, Goodbye!")
            break
        else:
            print("Invalid choice. Please Enter a number between 1 and 6.")

if __name__ == "__main__":
    main()           





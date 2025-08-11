import csv
import os

FILENAME = 'contacts.csv'

if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Name','Phone','Email'])
        
def add_contact():
    name = input("Enter Name :- ").strip()
    phone = input('Enter Phone Number :- ').strip()
    email = input('Enter Email :- ').strip()
    
    with open(FILENAME, 'r', encoding='utf-8') as f :
        reader = csv.DictReader(f)
        for row in reader:
            if row['Name'].lower() == name.lower():
                print("Contact already exists.")
                return 
            
    with open(FILENAME, 'a', encoding='utf-8',newline="") as f :
        writer = csv.writer(f)
        writer.writerow([name,phone,email])
        print('Contact Added Successfully!')
        
def view_contacts():
    # Read file and remove empty lines
    with open(FILENAME, 'r', encoding='utf-8') as f:
        lines = [line for line in f if line.strip()]

    # Save cleaned file
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    if not lines or len(lines) < 2:
        print("No contacts found.")
        return

    # Display contacts
    reader = csv.reader(lines)
    header = next(reader, None)  # Skip header
    contacts = list(reader)

    print(f"\nYour Contacts ({len(contacts)}):\n")
    for row in contacts:
        name = row[0] if len(row) > 0 else "N/A"
        phone = row[1] if len(row) > 1 else "N/A"
        email = row[2] if len(row) > 2 else "N/A"
        print(f'Name: {name}, Phone: {phone}, Email: {email}')
    print()

        
def search_contact():
    name = input("Enter Name to Search :- ").strip().lower()
    found = False
    
    with open(FILENAME, 'r', encoding='utf-8') as f :
        reader = csv.DictReader(f)
        for row in reader:
            if name == row['Name'].lower():
                print(f"{row['Name']} Found in Contacts")
                print(f"Name: {row['Name']}, Phone: {row['Phone']}, Email: {row['Email']}")
                found = True
                break
            
    if not found:
        print("Contact not Found.")
        
        
def delete_contact():
    name = input("Enter Name to Search :- ").strip().lower()
    deleted = False
    contacts = []
    
    with open(FILENAME, 'r', encoding='utf-8') as f :
        reader = csv.DictReader(f)
        for row in reader:
            if name == row['Name'].lower():
                print(f"{row['Name']} Deleted From Contacts")
                deleted = True
                continue
            contacts.append(row)
            
    if deleted:
        with open(FILENAME, 'w', encoding='utf-8') as f :
            writer = csv.DictWriter(f, fieldnames=['Name', 'Phone', 'Email'])
            writer.writeheader()
            writer.writerows(contacts)
                
def update_contact():
    name = input("Enter Name to Search :- ").strip().lower()
    updated_row = None
    contacts = []
    
    with open(FILENAME, 'r', encoding='utf-8') as f :
        reader = csv.DictReader(f)
        for row in reader:
            if name == row['Name'].lower():
                print(f"{row['Name']} Found in Contacts")
                updated_row = row
                continue
            contacts.append(row)
            
    if updated_row:
        new_name = input("Enter New Name (leave blank to keep unchanged): ").strip()
        new_phone = input("Enter New Phone (leave blank to keep unchanged): ").strip()
        new_email = input("Enter New Email (leave blank to keep unchanged): ").strip()
        
        if new_name:
            updated_row['Name'] = new_name
        if new_phone:
            updated_row['Phone'] = new_phone
        if new_email:
            updated_row['Email'] = new_email
            
        contacts.append(updated_row)
        
        with open(FILENAME, 'w', encoding='utf-8') as f :
            writer = csv.DictWriter(f, fieldnames=['Name', 'Phone', 'Email'])
            writer.writeheader()
            writer.writerows(contacts)
            
        print(f"{updated_row['Name']} Updated Successfully!")
    else:
        print("Contact not Found.")
        
        
def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            update_contact()
        elif choice == '6':
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice, please try again.")
            
if __name__ == "__main__":
    main()
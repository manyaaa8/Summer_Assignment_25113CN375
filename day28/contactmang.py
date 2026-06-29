print("**************** CONTACT MANAGEMENT SYSTEM ****************")
contacts = [[101, "Rahul", 9876543210, "rahul@gmail.com"],
    [102, "Priya", 9876501234, "priya@gmail.com"],
    [103, "Amit", 9876511111, "amit@gmail.com"]]
def add_contact():
    contact_id = int(input("ENTER CONTACT ID : "))
    for contact in contacts:
        if contact[0] == contact_id:
            print("CONTACT ID ALREADY EXISTS")
            return
    name = input("ENTER NAME : ")
    mobile = int(input("ENTER MOBILE NUMBER : "))
    email = input("ENTER EMAIL : ")
    contacts.append([contact_id, name, mobile, email])
    print("CONTACT ADDED SUCCESSFULLY")
def display_contacts():
    if len(contacts) == 0:
        print("NO CONTACTS AVAILABLE")
    else:
        print("\nID\tNAME\tMOBILE\t\tEMAIL")
        for contact in contacts:
            print(contact[0], "\t", contact[1], "\t", contact[2], "\t", contact[3])
def search_contact():
    contact_id = int(input("ENTER CONTACT ID : "))
    for contact in contacts:
        if contact[0] == contact_id:
            print("CONTACT FOUND")
            print("ID :", contact[0])
            print("NAME :", contact[1])
            print("MOBILE :", contact[2])
            print("EMAIL :", contact[3])
            return
    print("CONTACT NOT FOUND")
def update_contact():
    contact_id = int(input("ENTER CONTACT ID : "))
    for contact in contacts:
        if contact[0] == contact_id:
            contact[1] = input("ENTER NEW NAME : ")
            contact[2] = int(input("ENTER NEW MOBILE NUMBER : "))
            contact[3] = input("ENTER NEW EMAIL : ")
            print("CONTACT UPDATED SUCCESSFULLY")
            return
    print("CONTACT NOT FOUND")
def delete_contact():
    contact_id = int(input("ENTER CONTACT ID : "))
    for contact in contacts:
        if contact[0] == contact_id:
            contacts.remove(contact)
            print("CONTACT DELETED SUCCESSFULLY")
            return
    print("CONTACT NOT FOUND")

while True:
    print("1. ADD CONTACT")
    print("2. DISPLAY CONTACTS")
    print("3. SEARCH CONTACT")
    print("4. UPDATE CONTACT")
    print("5. DELETE CONTACT")
    print("6. EXIT")
    choice = int(input("ENTER YOUR CHOICE : "))
    if choice == 1:
        add_contact()
    elif choice == 2:
        display_contacts()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        print("THANK YOU FOR USING CONTACT MANAGEMENT SYSTEM")
        break
    else:
        print("INVALID CHOICE")
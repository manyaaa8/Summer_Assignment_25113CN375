print("**************** MINI HOTEL MANAGEMENT SYSTEM ****************")
hotel = [ ["101", "Rahul", 3, "AC"],
    ["102", "Priya", 2, "NON-AC"]]

def add_customer():
    room_no = input("ENTER THE ROOM NUMBER : ")
    name = input("ENTER THE CUSTOMER NAME : ")
    days = int(input("ENTER THE NUMBER OF DAYS : "))
    room_type = input("ENTER THE ROOM TYPE (AC/NON-AC) : ")
    hotel.append([room_no, name, days, room_type])
    print("CUSTOMER RECORD ADDED SUCCESSFULLY!")

def display():
    if hotel == []:
        print("NO CUSTOMER RECORD FOUND!")
    else:
        print("\nROOM NO\tNAME\tDAYS\tROOM TYPE")
        for i in hotel:
            print(i[0], "\t", i[1], "\t", i[2], "\t", i[3])

def search():
    room_no = input("ENTER THE ROOM NUMBER TO SEARCH : ")
    for i in hotel:
        if i[0] == room_no:
            print("ROOM NUMBER :", i[0])
            print("CUSTOMER NAME :", i[1])
            print("NUMBER OF DAYS :", i[2])
            print("ROOM TYPE :", i[3])
            return
    print("CUSTOMER RECORD NOT FOUND!")

def update():
    room_no = input("ENTER THE ROOM NUMBER TO UPDATE : ")
    for i in hotel:
        if i[0] == room_no:
            i[1] = input("ENTER NEW CUSTOMER NAME : ")
            i[2] = int(input("ENTER NEW NUMBER OF DAYS : "))
            i[3] = input("ENTER NEW ROOM TYPE : ")
            print("CUSTOMER RECORD UPDATED SUCCESSFULLY!")
            return
    print("CUSTOMER RECORD NOT FOUND!")

def delete():
    room_no = input("ENTER THE ROOM NUMBER TO DELETE : ")
    for i in hotel:
        if i[0] == room_no:
            hotel.remove(i)
            print("CUSTOMER RECORD DELETED SUCCESSFULLY!")
            return
    print("CUSTOMER RECORD NOT FOUND!")

while True:
    
    print("1. ADD CUSTOMER")
    print("2. DISPLAY CUSTOMERS")
    print("3. SEARCH CUSTOMER")
    print("4. UPDATE CUSTOMER")
    print("5. DELETE CUSTOMER")
    print("6. EXIT")
    ch = int(input("ENTER YOUR CHOICE : "))
    if ch == 1:
        add_customer()
    elif ch == 2:
        display()
    elif ch == 3:
        search()
    elif ch == 4:
        update()
    elif ch == 5:
        delete()
    elif ch == 6:
        print("THANK YOU!")
        break
    else:
        print("INVALID CHOICE!")
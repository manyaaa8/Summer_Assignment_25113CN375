print("**************** MINI LIBRARY MANAGEMENT SYSTEM ****************")
library = []

def add_book():
    book_id = input("ENTER THE BOOK ID : ")
    book_name = input("ENTER THE BOOK NAME : ")
    author = input("ENTER THE AUTHOR NAME : ")
    quantity = int(input("ENTER THE QUANTITY : "))
    library.append([book_id, book_name, author, quantity])
    print("BOOK ADDED SUCCESSFULLY!")

def display():
    if library == []:
        print("NO BOOK RECORD FOUND!")
    else:
        print("\nBOOK ID\tBOOK NAME\tAUTHOR\tQUANTITY")
        for i in library:
            print(i[0], "\t", i[1], "\t", i[2], "\t", i[3])

def search():
    book_id = input("ENTER THE BOOK ID TO SEARCH : ")
    for i in library:
        if i[0] == book_id:
            print("BOOK ID :", i[0])
            print("BOOK NAME :", i[1])
            print("AUTHOR :", i[2])
            print("QUANTITY :", i[3])
            return
    print("BOOK NOT FOUND!")

def update():
    book_id = input("ENTER THE BOOK ID TO UPDATE : ")
    for i in library:
        if i[0] == book_id:
            i[1] = input("ENTER NEW BOOK NAME : ")
            i[2] = input("ENTER NEW AUTHOR NAME : ")
            i[3] = int(input("ENTER NEW QUANTITY : "))
            print("BOOK UPDATED SUCCESSFULLY!")
            return
    print("BOOK NOT FOUND!")

def delete():
    book_id = input("ENTER THE BOOK ID TO DELETE : ")
    for i in library:
        if i[0] == book_id:
            library.remove(i)
            print("BOOK DELETED SUCCESSFULLY!")
            return
    print("BOOK NOT FOUND!")

while True:
    
    print("1. ADD BOOK")
    print("2. DISPLAY BOOKS")
    print("3. SEARCH BOOK")
    print("4. UPDATE BOOK")
    print("5. DELETE BOOK")
    print("6. EXIT")
    ch = int(input("ENTER YOUR CHOICE : "))
    if ch == 1:
        add_book()
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
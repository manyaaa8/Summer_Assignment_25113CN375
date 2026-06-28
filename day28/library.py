print("**************** LIBRARY MANAGEMENT SYSTEM ****************")
library = [ [101, "Python", "Guido", 5],
    [102, "C Programming", "Dennis", 3],
    [103, "Data Structures", "Mark", 4]]
def add_book():
    book_id = int(input("ENTER BOOK ID : "))

    for book in library:
        if book[0] == book_id:
            print("BOOK ID ALREADY EXISTS.")
            return
    name = input("ENTER BOOK NAME : ")
    author = input("ENTER AUTHOR NAME : ")
    quantity = int(input("ENTER QUANTITY : "))
    library.append([book_id, name, author, quantity])
    print("BOOK ADDED SUCCESSFULLY.")

def display_books():
    if len(library) == 0:
        print("NO BOOKS AVAILABLE.")
    else:
        print("\nID\tBOOK NAME\tAUTHOR\t\tQUANTITY")
        for book in library:
            for i in book:
             print(i,end="\n")
            print()
def search_book():
    book_id = int(input("ENTER BOOK ID TO SEARCH : "))
    for book in library:
        if book[0] == book_id:
            print("BOOK FOUND")
            print("ID :", book[0])
            print("NAME :", book[1])
            print("AUTHOR :", book[2])
            print("QUANTITY :", book[3])
            return
    print("BOOK NOT FOUND.")


def issue_book():
    book_id = int(input("ENTER BOOK ID : "))

    for book in library:
        if book[0] == book_id:
            if book[3] > 0:
                book[3] -= 1
                print("BOOK ISSUED SUCCESSFULLY.")
            else:
                print("BOOK NOT AVAILABLE.")
            return

    print("BOOK NOT FOUND.")
def return_book():
    book_id = int(input("ENTER BOOK ID : "))

    for book in library:
        if book[0] == book_id:
            book[3] += 1
            print("BOOK RETURNED SUCCESSFULLY.")
            return

    print("BOOK NOT FOUND.")
def delete_book():
    book_id = int(input("ENTER BOOK ID : "))
    for book in library:
        if book[0] == book_id:
            library.remove(book)
            print("BOOK DELETED SUCCESSFULLY.")
            return
    print("BOOK NOT FOUND.")
while True:
    print("1. ADD BOOK")
    print("2. DISPLAY BOOKS")
    print("3. SEARCH BOOK")
    print("4. ISSUE BOOK")
    print("5. RETURN BOOK")
    print("6. DELETE BOOK")
    print("7. EXIT")

    choice = int(input("ENTER YOUR CHOICE : "))

    if choice == 1:
        add_book()

    elif choice == 2:
        display_books()

    elif choice == 3:
        search_book()

    elif choice == 4:
        issue_book()

    elif choice == 5:
        return_book()

    elif choice == 6:
        delete_book()

    elif choice == 7:
        print("THANK YOU FOR USING LIBRARY MANAGEMENT SYSTEM")
        break
    else:
        print("INVALID CHOICE")
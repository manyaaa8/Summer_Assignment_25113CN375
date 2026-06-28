print("*************** TICKET BOOKING SYSTEM ***************")

tickets = [
    [101, "Delhi to Mumbai", 1200, 20],
    [102, "Delhi to Jaipur", 800, 15],
    [103, "Delhi to Lucknow", 1000, 10]
]
def book_ticket():
    ticket_id = int(input("ENTER TICKET ID : "))
    for ticket in tickets:
        if ticket[0] == ticket_id:
            seats = int(input("ENTER NUMBER OF SEATS : "))
            if seats <= ticket[3]:
                total = seats * ticket[2]
                ticket[3] -= seats
                print("TICKET BOOKED SUCCESSFULLY")
                print("TOTAL AMOUNT :", total)
                print("REMAINING SEATS :", ticket[3])
            else:
                print("NOT ENOUGH SEATS AVAILABLE")
            return
    print("TICKET NOT FOUND")
def display_tickets():
    if len(tickets) == 0:
        print("NO TICKETS AVAILABLE")
    else:
        print("\nID\tROUTE\t\t\tPRICE\tNO.OF SEATS")
        for ticket in tickets:
            print(ticket[0],"\t" ticket[1],"\t" ticket[2],"\t" ticket[3])
def search_ticket():
    flag=0
    ticket_id = int(input("ENTER TICKET ID : "))
    for ticket in tickets:
        if ticket[0] == ticket_id:
            print("TICKET FOUND")
            print("ID :", ticket[0])
            print("ROUTE :", ticket[1])
            print("PRICE :", ticket[2])
            print("AVAILABLE SEATS :", ticket[3])
            flag=1
            break
    if flag==0:
     print("TICKET NOT FOUND")
def cancel_ticket():
    flag=0
    ticket_id = int(input("ENTER TICKET ID : "))
    for ticket in tickets:
        if ticket[0] == ticket_id:
            seats = int(input("ENTER NUMBER OF SEATS TO CANCEL : "))
            ticket[3] += seats
            print("TICKET CANCELLED SUCCESSFULLY")
            print("AVAILABLE SEATS :", ticket[3])
            flag=1
            break
    if flag==0:
        print("TICKET NOT FOUND")
def add_ticket():
    ticket_id = int(input("ENTER TICKET ID : "))
    for ticket in tickets:
        if ticket[0] == ticket_id:
            print("TICKET ID ALREADY EXISTS")
            break
    route = input("ENTER ROUTE : ")
    price = float(input("ENTER PRICE : "))
    seats = int(input("ENTER TOTAL SEATS : "))
    tickets.append([ticket_id, route, price, seats])
    print("TICKET ADDED SUCCESSFULLY")
def delete_ticket():
    flag=0
    ticket_id = int(input("ENTER TICKET ID : "))
    for ticket in tickets:
        if ticket[0] == ticket_id:
            tickets.remove(ticket)
            print("TICKET DELETED SUCCESSFULLY")
            flag=1
            break
    if flag==0:
     print("TICKET NOT FOUND")
while True:

    print("1. ADD TICKET")
    print("2. DISPLAY TICKETS")
    print("3. SEARCH TICKET")
    print("4. BOOK TICKET")
    print("5. CANCEL TICKET")
    print("6. DELETE TICKET")
    print("7. EXIT")
    choice = int(input("ENTER YOUR CHOICE : "))
    if choice == 1:
        add_ticket()
    elif choice == 2:
        display_tickets()
    elif choice == 3:
        search_ticket()
    elif choice == 4:
        book_ticket()
    elif choice == 5:
        cancel_ticket()
    elif choice == 6:
        delete_ticket()
    elif choice == 7:
        print("THANK YOU FOR USING TICKET BOOKING SYSTEM")
        break
    else:
        print("INVALID CHOICE")
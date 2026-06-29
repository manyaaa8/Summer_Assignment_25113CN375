print("**************** ATM SIMULATION SYSTEM ****************")
accounts = [[1234, "Rahul", 50000],
    [5678, "Priya", 75000],
    [9012, "Amit", 30000]]
def check_balance():
    pin = int(input("ENTER PIN : "))

    for account in accounts:
        if account[0] == pin:
            print("ACCOUNT HOLDER :", account[1])
            print("CURRENT BALANCE :", account[2])
            return
    print("INVALID PIN")
def deposit():
    pin = int(input("ENTER PIN : "))
    for account in accounts:
        if account[0] == pin:
            amount = float(input("ENTER AMOUNT TO DEPOSIT : "))
            if amount <= 0:
                print("INVALID AMOUNT")
                return
            account[2] += amount
            print("AMOUNT DEPOSITED SUCCESSFULLY")
            print("NEW BALANCE :", account[2])
            return
    print("INVALID PIN")
def withdraw():
    pin = int(input("ENTER PIN : "))

    for account in accounts:
        if account[0] == pin:
            amount = float(input("ENTER AMOUNT TO WITHDRAW : "))

            if amount <= 0:
                print("INVALID AMOUNT")
                return

            if amount <= account[2]:
                account[2] -= amount
                print("AMOUNT WITHDRAWN SUCCESSFULLY")
                print("REMAINING BALANCE :", account[2])
            else:
                print("INSUFFICIENT BALANCE")
            return
    print("INVALID PIN")
def change_pin():
    old_pin = int(input("ENTER CURRENT PIN : "))
    for account in accounts:
        if account[0] == old_pin:
            new_pin = int(input("ENTER NEW PIN : "))
            for acc in accounts:
                if acc[0] == new_pin:
                    print("PIN ALREADY EXISTS")
                    return
            account[0] = new_pin
            print("PIN CHANGED SUCCESSFULLY")
            return
    print("INVALID PIN")
def display_accounts():
    print("\nPIN\tNAME\tBALANCE")
    for account in accounts:
        print(account[0], "\t", account[1], "\t", account[2])

while True:
    print("1. CHECK BALANCE")
    print("2. DEPOSIT")
    print("3. WITHDRAW")
    print("4. CHANGE PIN")
    print("5. DISPLAY ACCOUNTS")
    print("6. EXIT")
    choice = int(input("ENTER YOUR CHOICE : "))
    if choice == 1:
        check_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        change_pin()
    elif choice == 5:
        display_accounts()
    elif choice == 6:
        print("THANK YOU FOR USING ATM SIMULATION SYSTEM")
        break
    else:
        print("INVALID CHOICE")
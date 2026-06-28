print("**************** BANK ACCOUNT SYSTEM ****************")
bank = [[1001, "Rahul", 50000, 9876543210],
    [1002, "Priya", 75000, 9876501234]]

def create_account():
    acc_no = int(input("ENTER ACCOUNT NUMBER : "))
    for account in bank:
        if account[0] == acc_no:
            print("ACCOUNT NUMBER ALREADY EXISTS.")
            return
    name = input("ENTER ACCOUNT HOLDER NAME : ")
    balance = float(input("ENTER INITIAL BALANCE : "))
    mobile = int(input("ENTER MOBILE NUMBER : "))
    bank.append([acc_no, name, balance, mobile])
    print("ACCOUNT CREATED SUCCESSFULLY.")
def display_accounts():
    if len(bank) == 0:
        print("NO ACCOUNTS FOUND.")
    else:
        print("\nACC NO\tNAME\tBALANCE\tMOBILE")
        for account in bank:
            for i in account:
             print(i,end="\t")
def search_account():
    acc_no = int(input("ENTER ACCOUNT NUMBER : "))

    for account in bank:
        if account[0] == acc_no:
            print("ACCOUNT FOUND")
            print("ACCOUNT NUMBER :", account[0])
            print("NAME :", account[1])
            print("BALANCE :", account[2])
            print("MOBILE :", account[3])
            return

    print("ACCOUNT NOT FOUND.")


def deposit():
    acc_no = int(input("ENTER ACCOUNT NUMBER : "))

    for account in bank:
        if account[0] == acc_no:
            amount = float(input("ENTER AMOUNT TO DEPOSIT : "))
            account[2] += amount
            print("AMOUNT DEPOSITED SUCCESSFULLY.")
            print("NEW BALANCE :", account[2])
            return
    print("ACCOUNT NOT FOUND.")
def withdraw():
    acc_no = int(input("ENTER ACCOUNT NUMBER : "))
    for account in bank:
        if account[0] == acc_no:
            amount = float(input("ENTER AMOUNT TO WITHDRAW : "))
            if amount <= account[2]:
                account[2] -= amount
                print("AMOUNT WITHDRAWN SUCCESSFULLY.")
                print("NEW BALANCE :", account[2])
            else:
                print("INSUFFICIENT BALANCE.")
            return
    print("ACCOUNT NOT FOUND.")
def delete_account():
    acc_no = int(input("ENTER ACCOUNT NUMBER : "))
    for account in bank:
        if account[0] == acc_no:
            bank.remove(account)
            print("ACCOUNT DELETED SUCCESSFULLY.")
            return
    print("ACCOUNT NOT FOUND.")
def check_balance():
    acc_no = int(input("ENTER ACCOUNT NUMBER : "))
    for account in bank:
        if account[0] == acc_no:
            print("CURRENT BALANCE :", account[2])
            return

    print("ACCOUNT NOT FOUND.")


while True:

    print("\n******** MENU ********")
    print("1. CREATE ACCOUNT")
    print("2. DISPLAY ALL ACCOUNTS")
    print("3. SEARCH ACCOUNT")
    print("4. DEPOSIT MONEY")
    print("5. WITHDRAW MONEY")
    print("6. DELETE ACCOUNT")
    print("7. CHECK BALANCE")
    print("8. EXIT")

    choice = int(input("ENTER YOUR CHOICE : "))
    if choice == 1:
        create_account()
    elif choice == 2:
        display_accounts()
    elif choice == 3:
        search_account()
    elif choice == 4:
        deposit()
    elif choice == 5:
        withdraw()
    elif choice == 6:
        delete_account()
    elif choice == 7:
        check_balance()
    elif choice == 8:
        print("THANK YOU FOR USING BANK ACCOUNT SYSTEM")
        break
    else:
        print("INVALID CHOICE")
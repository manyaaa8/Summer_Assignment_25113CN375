print("******** INVENTORY MANAGEMENT SYSTEM ********")

inventory = [[101, "Laptop", 10, 50000],
    [102, "Mouse", 20, 500],
    [103, "Keyboard", 15, 1200]]

def add_product():
    product_id = int(input("ENTER PRODUCT ID: "))
    for product in inventory:
        if product[0] == product_id:
            print("PRODUCT ID ALREADY EXISTS")
            return
    name = input("ENTER PRODUCT NAME: ")
    quantity = int(input("ENTER QUANTITY: "))
    price = float(input("ENTER PRICE: "))
    inventory.append([product_id, name, quantity, price])
    print("PRODUCT ADDED SUCCESSFULLY")

def display_products():
    if len(inventory) == 0:
        print("INVENTORY IS EMPTY")
    else:
        print("\nID\tNAME\t\tQUANTITY\tPRICE")
        for product in inventory:
            print(product[0], "\t", product[1], "\t\t", product[2], "\t\t", product[3])

def search_product():
    product_id = int(input("ENTER PRODUCT ID: "))
    for product in inventory:
        if product[0] == product_id:
            print("PRODUCT FOUND")
            print("ID:", product[0])
            print("NAME:", product[1])
            print("QUANTITY:", product[2])
            print("PRICE:", product[3])
            return
    print("PRODUCT NOT FOUND")

def update_product():
    product_id = int(input("ENTER PRODUCT ID: "))
    for product in inventory:
        if product[0] == product_id:
            product[1] = input("ENTER NEW PRODUCT NAME: ")
            product[2] = int(input("ENTER NEW QUANTITY: "))
            product[3] = float(input("ENTER NEW PRICE: "))
            print("PRODUCT UPDATED SUCCESSFULLY")
            return
    print("PRODUCT NOT FOUND")

def delete_product():
    product_id = int(input("ENTER PRODUCT ID: "))
    for product in inventory:
        if product[0] == product_id:
            inventory.remove(product)
            print("PRODUCT DELETED SUCCESSFULLY")
            return
    print("PRODUCT NOT FOUND")

def increase_stock():
    product_id = int(input("ENTER PRODUCT ID: "))
    for product in inventory:
        if product[0] == product_id:
            qty = int(input("ENTER QUANTITY TO ADD: "))
            product[2] += qty
            print("STOCK UPDATED SUCCESSFULLY")
            print("NEW QUANTITY:", product[2])
            return
    print("PRODUCT NOT FOUND")

def reduce_stock():
    product_id = int(input("ENTER PRODUCT ID: "))
    for product in inventory:
        if product[0] == product_id:
            qty = int(input("ENTER QUANTITY TO REDUCE: "))
            if qty <= product[2]:
                product[2] -= qty
                print("STOCK UPDATED SUCCESSFULLY")
                print("REMAINING QUANTITY:", product[2])
            else:
                print("INSUFFICIENT STOCK")
            return
    print("PRODUCT NOT FOUND")

def total_value():
    if len(inventory) == 0:
        print("INVENTORY IS EMPTY")
    else:
        total = 0
        for product in inventory:
            total += product[2] * product[3]
        print("TOTAL INVENTORY VALUE:", total)

def count_products():
    print("TOTAL PRODUCTS:", len(inventory))

while True:

    print("1. Add Product")
    print("2. Display Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Increase Stock")
    print("7. Reduce Stock")
    print("8. Total Inventory Value")
    print("9. Count Products")
    print("10. Exit")
    choice = int(input("ENTER YOUR CHOICE: "))
    if choice == 1:
        add_product()
    elif choice == 2:
        display_products()
    elif choice == 3:
        search_product()
    elif choice == 4:
        update_product()
    elif choice == 5:
        delete_product()
    elif choice == 6:
        increase_stock()
    elif choice == 7:
        reduce_stock()
    elif choice == 8:
        total_value()
    elif choice == 9:
        count_products()
    elif choice == 10:
        print("THANK YOU!")
        break
    else:
        print("INVALID CHOICE")
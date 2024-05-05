from datetime import datetime

# Define the checkout system function
def main():
    # Initialize variables
    counter = 0
    total = 1
    sub_total = 0
    items = []
    quantity = []
    price = []
    totals = []

    # Get customer's name
    customer_name = input("What is the customer's name? ")

    # Get user's response for buying items
    user_response = ""
    today = datetime.today()

    while user_response != "no":
        # Get item bought, quantity, and price per unit
        item_bought = input("What did the user buy? ")
        number_of_pieces = int(input("How many pieces of goods? "))
        price_per_unit = int(input("How much per unit? "))
        user_response = input("Add more items? (yes/no) ")

        # Calculate total for the item
        total = number_of_pieces * price_per_unit

        # Add item details to lists
        items.append(item_bought)
        quantity.append(number_of_pieces)
        price.append(price_per_unit)
        totals.append(total)

    # Get cashier's name and discount given
    cashier_name = input("What is your name? ")
    discount_given = int(input("How much discount will he get? "))

    # Print store details and transaction information
    print("SEMICOLON STORES")
    print("MAIN BRANCH")
    print("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABO, LAGOS")
    print("TEL: 03293828343")
    print(today)
    print("Cashier:", cashier_name)
    print("Customer's Name:", customer_name)

    print("=================================")
    print("ITEM \t QTY \t PRICE \t  TOTAL")
    print("----------------------------------")
    
    # Print each item's details
    for counter in range(len(items)):
        print(items[counter], "\t", quantity[counter], "\t", price[counter], "\t", totals[counter])
        sub_total += totals[counter]

    # Calculate discount, VAT, and total bill
    discount = discount_given * sub_total / 100
    vat = 17.50 / 100 * sub_total
    bill_total = sub_total + discount + vat

    print("--------------------------------------")
    print("\tSub Total:\t", sub_total)
    print("\tDiscount:\t", discount)
    print("\tVAT @17.50:\t", vat)
    print("--------------------------------------")
    print("\tBill Total:\t", bill_total)

    print("=================================")
    print("THIS IS NOT A RECEIPT, KINDLY PAY", bill_total)
    print("=================================")

    # Get amount paid by the customer
    amount_paid = float(input("How much did the customer give to you? "))
    balance = bill_total - amount_paid

    # Print transaction details with payment information
    print("SEMICOLON STORES")
    print("MAIN BRANCH")
    print("LOCATION: 312, HERBERT MACAULAY WAY, SABO YABO, LAGOS")
    print("TEL: 03293828343")
    print(today)
    print("Cashier:", cashier_name)
    print("Customer's Name:", customer_name)

    print("=================================")
    print("ITEM \t QTY \t PRICE \t  TOTAL")
    print("----------------------------------")

    print("--------------------------------------")
    print("\tSub Total:\t", sub_total)
    print("\tDiscount:\t", discount)
    print("\tVAT @17.50:\t", vat)
    print("--------------------------------------")
    print("\tBill Total:\t", bill_total)
    print("\tAmount Paid:\t", amount_paid)
    print("\tBalance:\t", balance)
    print("=================================")
    print("THANK YOU FOR YOUR PATRONAGE")
    print("=================================")

# Call the main function
main()
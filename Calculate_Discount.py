price = float(input("Enter a Price: "))
disc = float(input("Enter a Discount: "))
discount = (price * (disc/100))
discount_price = price - discount
print("Discount Price: ",discount_price)
print("WElCOME TO E-STORE: ")
custormer_name = input("Please Enter Custormer Name: ")
number_of_items = int(input ("Please Enter Number Of Items Purchased: "))
percentage_discount = float(input ("Please Enter Percentage Discount: "))

total_cost = 0;

for i in range (1,  number_of_items + 1) :
	item_price = int(input(f"Please Enter cost for item {i}: "))
	
	total_cost += item_price


print("\n" + "Customer Name: " + str(custormer_name) + "\n" +  "Number Of Items Bought: " +  str(number_of_items) + "\n" + "Percentage Discount: " + str(percentage_discount) + "\n")

print("Original Cost: " + str(total_cost) + "\n")



if total_cost >= 200 :

	discount =   total_cost * (percentage_discount / 100) 

	discounted_cost = total_cost - discount

	print("Discounted Cost: ", discounted_cost)


elif total_cost <= 200 :

	print( "\n" + "Discounted Cost: 0 (no discount added)  ")

print( "\n" + "Thanks For Your Patronage  ")



	

	







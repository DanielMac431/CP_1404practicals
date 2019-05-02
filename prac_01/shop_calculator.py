total_price = 0
number_of_items = int(input("Number of Items: "))
for i in range(0, number_of_items, 1):
    price_of_item = float(input("Price of item: "))
    while price_of_item <= 0:
        print("Invalid Input")
        price_of_item = float(input("Price of item: "))
    total_price = total_price + price_of_item
if total_price > 100:
    total_price = total_price*0.9
print("Total Price: ${:.2f} ".format(total_price))


total_price = 0
number_of_items = int(input("Number of Items: "))
for i in range(0, number_of_items, 1):
    while True:
        price_of_item = float(input("Price of item: "))
        if price_of_item > 0:
            total_price = total_price + price_of_item
            break
        else:
            print("Invalid Input")
            number_of_items = number_of_items + 1
if total_price > 100:
    total_price = total_price*0.9
print("Total Price: ${:.2f} ".format(total_price))


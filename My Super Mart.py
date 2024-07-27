items = {"Laptop":100000, 'Mobile':50000, 'Printer':30000, 'Head Phone':15000, 'Speaker':5000}
print("Hey! Welcome To My Super Mart")
order = input("Enter an item: ")
discount = 20
total_price = 0
if order in items:
    total_price += items[order]
    print(f"You ordered: {order}")
user = input("Do you want to buy further more items? ")
if user == "Yes":
    order_2 = input("Enter an item: ")
    if order_2 in items:
        total_price += items[order_2]
        print(f"You ordered: {order_2}")
    else:
        print(f"{order} is not available yet.")
if total_price >= 100000:
    print(f"Your total price is: {total_price}")
    print(f"Discounted Price: {total_price * (1 - discount/100)}")
elif total_price < 100000:
    print(f"Your total price is: {total_price}")
    print(f"Your total price is not eligible for discount. Thank you!")
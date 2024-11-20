items = {"Laptop":100000, 'Mobile':50000, 'Printer':30000, 'Head Phone':15000, 'Speaker':5000}
print("Hey! Welcome To My Super Mart")
discount = 20
total_price = 0
while True:
    order = input("Enter an item: ")
    if order in items:
        total_price += items[order]
        print(f"You ordered: {order} Price: {items[order]}")
    else:
        print(f"{order} is not available yet.")

    user = input("Do you want to buy further more items? ")
    if user == "NO":
        break

if total_price >= 100000:
    print(f"Your total bill is: {total_price}")
    print(f"After Discount Price: {total_price * (1 - discount/100)}")
    print(f"Thank You For Shopping!")
elif total_price < 100000:
    print(f"Your total price is: {total_price} ")
    print(f"Your total price is not eligible for discount. Thank you!")

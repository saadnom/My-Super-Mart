import pandas as pd

data = pd.read_excel('grocessory_200_products.xlsx')
# print(data)

item = data['ITEMS']
price = data['PRICE']

items = dict(zip(item,price))
# print(items)

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

if total_price >= 50000:
    print(f"Your total bill is: {total_price}")
    print(f"After Discount Price: {total_price * (1 - discount/100)}")
    print(f"Thank You For Shopping!")
elif total_price < 50000:
    print(f"Your total price is: {total_price} ")
    print(f"Your total price is not eligible for discount. Thank you!")
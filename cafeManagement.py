menu = {
    "pizza": 40,
    "pasta": 120,
    "coffee": 230,
    "truffle": 200,
    "iced latte": 230,
    "salad": 80,
    "burger": 120,
    "choco lava cake": 230
}

#Greet
print("welcome to our restuarant")
print("pizza: Rs40\npasta: Rs120\ncoffee: Rs230\ntruffle: Rs200\niced latte: Rs230\nsalad: Rs80\nburger: Rs120\nchoco lava cake:Rs230")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
    
else:
    print(f"ordered item {item_1} is not available yet!")

another_order = input("do you want to add another item? (yes/no)")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2}has been added to order")
    else:
        print(f"ordered item {item_2} is not available!")

print(f"the total amount of items to pay is {order_total}")
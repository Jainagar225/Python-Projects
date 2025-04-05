#Concession stand program 

menu = { "Pizza" : 220.0,
         "Nachos" : 140.0,
         "Popcorn": 120.0,
         "Fries" : 140.0,
         "Chips" : 100.0,
         "Pretzel" : 180.0,
         "Lemonade" : 120.0}

cart = []
total = 0

print("-------- MENU --------")

for key, value in menu.items():
    print(f"{key:9} : ₹{value:.2f}")

print("----------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food) 

for food in cart:
    total += menu.get(food)
    print(food, end = "")

print()
print(f"Total is : ₹{total:.2f}")
menu = {
    "pizza": 180,
    "burger": 60,
    "chowmin": 70,
    "fried_chilli_momos": 70,
    "momos": 70,
    "thupka": 60,
    "pasta": 60,
    "coffee": 30,
    "juice": 70,
    "chai": 20,
}
total = 0 
print("======MENU==============")

for item, price in menu.items():
    print(f"{item.title():100} ₹{price}")

print("=========================")

while True:
    user = input("Your Order (X To Exit Menu) :- ").lower()
    if user == "x":
        print(f"Thanks For Visiting Us Your Total Is {total}")
        break

    if user in menu:
        total += menu[user]
        print(f"The Price Of {user} Will Be ₹{menu[user]}")
        print(f"Your Total Is {total}")
    else:
        print(f"Sorry, {user} Is Not Available Right Now")
			
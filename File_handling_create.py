# Interface
print("[--------------###############--------------]")
print("[--------------###############--------------]")
print("[--------------####GAMESYU####--------------]")
print("[--------------###############--------------]")
print("[--------------###############--------------]\n")

print("WHAT'S YOUR NAME?\n")
name = input("Enter Your Name 👾 :- ")

print(f"{name}, press X to save your data.")
print(f"{name}, press Y to continue without saving.")

saving = input("Enter Here :- ").lower()

if saving == "x":
    file = open("GAMESYU.txt", "w")
    file.write(f"Name: {name}\n")
    file.close()
    print("✅ Data saved!")
elif saving == "y":
    print("❌ Data not saved.")
else:
    print("Invalid choice.")

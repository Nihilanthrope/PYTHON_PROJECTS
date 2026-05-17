import random 

number_guessing_start = random.randint(1, 100)

while True: 
    try:
        guess = int(input("Guess The Number between 1 to 100 easy hai: "))

        if guess > number_guessing_start:
            print("Too high randwe 🖕")
            
        elif guess < number_guessing_start:
            print("Too low chutiya🖕") 
            
        else:
            print("Galti se jeeta hai lawde🤡🖕")
            break

    except ValueError:
        print("Gawar hai Kya maderchod 🙏")
        
        
        #2nd project 😭😭🙏
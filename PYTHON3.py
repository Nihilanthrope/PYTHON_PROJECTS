
n = int(input("Please Enter Your Number :- "))
total = 0

        #print even or odd 
if n%2 ==0:
    print (f"{n} is An even number - ")
else:
    print(f"{n} is an odd number ")
    
        #print sum of digits
 
for i in str(n):
    total += int(i)
    print("Sum of digits are",total)
    
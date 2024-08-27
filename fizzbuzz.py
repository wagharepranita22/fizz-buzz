import random
print("WELCOME TO FIZZ BUZZ")
x = random.randint(1,100)

if x%3 == 0 and x%5 == 0:
    print("FIZZ BUZZ" ,end= " ")
elif x % 3 == 0:
    print("FIZZ", end=" ")
elif x % 5 == 0:
    print("BUZZ", end=" ")
else:
    print(x, end=" ")

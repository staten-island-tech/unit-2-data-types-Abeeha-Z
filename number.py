import random
import math
n= random.randint(1, 10)
x = int(input("Guess the number: "))
    if(x > n):
        print("Lower")
    else:
        print("Higher")
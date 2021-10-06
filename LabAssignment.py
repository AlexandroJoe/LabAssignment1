import random
import math


upper = int(input("Insert highest number :"))
lower = int(input("Insert lowest number : "))
num = random.randint(lower, upper)

count = 0
while count < 10 :
    count += 1
    guess = int(input("Insert your number : "))
    if guess == num :
        print ("correct number")
        break
    elif guess > num :
        print ("the number is too big")
    elif guess < num :
        print ("the number is too small")

    if count >= 10 :
        print ("try rerun")








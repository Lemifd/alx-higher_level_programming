#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
size = len(str(number))
l_d = int(number[size-1])
number = int(number)
if l_d > 5:
    print(f"Last digit of {number:d} is {l_d} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number:d} is {l_d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {l_d} and is 0")

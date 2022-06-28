#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    l_d = number % -10
else:
    l_d = number % 10
print('Last digit of', number, 'is', l_d, end=' ')
if l_d > 5:
    print(f"Last digit of {number:d} is {l_d} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number:d} is {l_d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {l_d} and is 0")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_n = abs(number) % 10
if number < 0:
    last_n = last_n * -1
string_1 = "Last digit of {} is {} and is greater than 5"
string_2 = "Last digit of {} is {} and is less than 6 and not 0"
if last_n > 5:
    print(string_1.format(number, last_n))
elif last_n < 6 and last_n != 0:
    print(string_2.format(number, last_n))
else:
    print("Last digit of {} is {} and is 0".format(number, last_n))

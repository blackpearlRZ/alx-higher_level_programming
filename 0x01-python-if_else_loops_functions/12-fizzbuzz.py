#!/usr/bin/python3
# If num divisible by 3, print fizz
# .............   by 5, print buzz
# ...............3 n 5 print fizz buzz

def fizzbuzz():
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
        if not output:
            output = str(i)
        print(output, end=' ')

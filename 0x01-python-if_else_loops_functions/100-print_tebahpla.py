#!/usr/bin/python3
for n in range(122, 96, -1):
    n = n - 32 if n % 2 else n
    print('{}'.format(chr(n)), end="")

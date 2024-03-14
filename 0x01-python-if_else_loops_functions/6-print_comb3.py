#!/usr/bin/python3
print(", ".join(["{}{}".format(i, n)
                 for i in range(0, 9)
                 for n in range(i + 1, 10)]))

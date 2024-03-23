#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    length = len(argv)
    for e in range(1, length):
        sum += int(argv[e])
    print("{}".format(sum))

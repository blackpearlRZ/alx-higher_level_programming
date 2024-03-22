#!/usr/bin/python3

def uppercase(str):
    final_res = "".join(["{}".format(chr(ord(c) - 32))
                        if 'a' <= c <= 'z' else c for c in str])
    print(final_res)

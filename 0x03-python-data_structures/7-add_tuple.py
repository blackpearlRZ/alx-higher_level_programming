#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    temp = tuple_a + (0, 0)
    temp2 = tuple_b + (0, 0)
    return temp[0] + temp2[0], temp[1] + temp2[1]

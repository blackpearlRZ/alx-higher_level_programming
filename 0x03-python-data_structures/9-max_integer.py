#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    big_int = my_list[0]
    for num in my_list:
        if num > big_int:
            big_int = num
    return big_int

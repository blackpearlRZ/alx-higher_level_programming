#!/usr/bin/python3
'''tryin divide and conquer'''

def find_peak(list_of_integers):
    '''divide and conquer'''
    if list_of_integers == []:
        return None

    list_len = len(list_of_integers)
    midoflist = int(list_len / 2)
    loi = list_of_integers

    if midoflist - 1 < 0 and midoflist + 1 >= list_len:
        return loi[midoflist]
    elif midoflist - 1 < 0:
        return loi[midoflist] if loi[midoflist] > loi[midoflist + 1] else loi[midoflist + 1]
    elif midoflist + 1 >= list_len:
        return loi[midoflist] if loi[midoflist] > loi[midoflist - 1] else loi[midoflist - 1]

    if loi[midoflist - 1] < loi[midoflist] > loi[midoflist + 1]:
        return loi[midoflist]

    if loi[midoflist + 1] > loi[midoflist - 1]:
        return find_peak(loi[midoflist:])
    return find_peak(loi[:midoflist])

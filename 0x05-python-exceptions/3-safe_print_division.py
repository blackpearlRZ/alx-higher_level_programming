#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resultu = a / b
    except ZeroDivisionError:
        resultu = None
    finally:
        print("Inside result: {}".format(resultu))
    return resultu

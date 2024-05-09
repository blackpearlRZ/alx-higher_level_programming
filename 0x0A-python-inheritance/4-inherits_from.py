#!/usr/bin/python3
'''shbang'''


def inherits_from(obj, a_class):
    '''u already know amigoo '''
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)

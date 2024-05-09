#!/usr/bin/python3
'''Defines an inherited list class MyList.'''


class MyList(list):
    ''' MyList class that inherits from list'''

    def print_sorted(self):
        ''' public method for sortin '''
        sorted_l = self.copy()
        sorted_l.sort()
        print(sorted_l)

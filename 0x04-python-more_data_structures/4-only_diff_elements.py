#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    temp_set_1 = set_1.difference(set_2)
    temp_set_2 = set_2.difference(set_1)
    final_set = temp_set_1.union(temp_set_2)
    return final_set

#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)       # OOB sanity check
    new_list = my_list[:]      # copy list
    new_list[idx] = element    # replace element
    return (new_list)

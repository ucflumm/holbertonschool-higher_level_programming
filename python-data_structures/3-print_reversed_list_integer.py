#!/usr/bin/python3

# No index?? testing try and catch

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))

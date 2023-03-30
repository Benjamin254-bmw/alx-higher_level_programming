#!/usr/bin/python3

"""
a function that prints the first x elements of a list and only integers.

Args:
    my_list (list): The list to print elements from.
    x (int): The number of elements of my_list to print.
Returns:
    The number of elements printed.
"""


def safe_print_list_integers(my_list=[], x=0):
    _num = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i], end=""))
            _num += 1
        except(ValueError, TypeError):
            continue
    print("")
    return(_num)

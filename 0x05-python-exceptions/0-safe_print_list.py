#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints x elements of a list
    All elements must be printed on the same line followed by a new line.
    x represents the number of elements to print
    x can be bigger than the length of my_list
    returns the real number of elements printed
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end=""))
            ret += 1
        except IndexError:
            break
        print("")
        return(ret)

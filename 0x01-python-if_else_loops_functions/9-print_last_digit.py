#!/usr/bin/python3
def print_las_digit_(number):
     if number < 0:
         number = number * -1
    r = number % 10
    print('{}'.format(r), end="")
    return r

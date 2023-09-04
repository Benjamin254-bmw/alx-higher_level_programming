#!/usr/bin/python3
"""defines a function that prints a name"""

def say_my_name(first_name, second_name=""):
    """
    print a name

    Args:
        first_name(str): first name to print
        second_name(str): second name to print
    Raises:
        TypeError: where either the first_name or last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(second_name, str):
        raise TypeError("second_name must be a string")
    print ("My name is {} {}".format(first_name, second_name))


#!/usr/bin/python3
"""defines an integer addition function"""

def add_integer(a, b=98):
    """return the integer addition of a and b
    float arguements are typecasted into integers before addition is performed

    Raises:
        TypeError: when both or either a or b are non-integer or non-float"""

    if((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")

    if((not isinstance(a, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return(int(a) + int(b))

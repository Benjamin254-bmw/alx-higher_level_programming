#!/usr/bin/python3
"""defines a locked class
"""


class LockedClass:
    """prevent the user from dynamically creating new instace
    attributes, except if the new instance attribte
    is called first_name
    """
    __slots__ = ["first_name"]

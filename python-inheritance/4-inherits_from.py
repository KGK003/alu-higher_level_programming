#!/usr/bin/python3
"""
Function to check if an object is an instance of a class that inherited from
the specified class (directly or indirectly).
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited from
    the specified class (directly or indirectly); otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

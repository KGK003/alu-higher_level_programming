#!/usr/bin/python3
"""
Module to retrieve all attributes and methods of an object.

This module contains a single function `lookup` that takes an object
as input and returns a list of all its attributes and methods using
the built-in `dir()` function.
"""


def lookup(obj):
    """
    Returns a list of all attributes and methods of the object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of strings representing the attributes and methods.
    """
    return dir(obj)

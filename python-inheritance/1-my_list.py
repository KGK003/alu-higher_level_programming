#!/usr/bin/python3
"""
Class MyList that inherits from list and includes a method print_sorted
which prints the list in sorted order (ascending).
"""

class MyList(list):
    """
    Inherits from list to add a method that prints the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order without modifying the original list.
        """
        print(sorted(self))

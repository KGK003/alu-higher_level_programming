#!/usr/bin/python3
#!/usr/bin/python3
class MyList(list):
    """
    A class that inherits from the built-in list class.
    Adds a method to print the list sorted.
    """


    def print_sorted(self):
        """
        Prints the list in ascending order (sorted).
        """
        print(sorted(self))

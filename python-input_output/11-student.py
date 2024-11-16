#!/usr/bin/python3
""" Student to JSON """


class Student:
    """ New class student """

 def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance."""
        if attrs is None:
            return self.__dict__  # Return all attributes as a dictionary
        else:
            # Return only the attributes in the attrs list
            return {key: value for key, value in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with values from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)

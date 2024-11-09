#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        # The method raises an exception with the message as required
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        # Validate that the value is an integer
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        
        # Validate that the value is greater than 0
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

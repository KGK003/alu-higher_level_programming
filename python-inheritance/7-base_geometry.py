#!/usr/bin/python3
class BaseGeometry:
    """Base class for geometry shapes."""
    
    def area(self):
        """Method to compute area. Raises an exception if not implemented."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates that value is an integer and greater than 0.
        
        Args:
            name (str): Name of the parameter being validated.
            value (int): The value to validate.
            
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

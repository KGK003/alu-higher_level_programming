#!/usr/bin/python3

"""
This module defines a function `matrix_divided` that divides all elements of a matrix
by a given divisor `div`, and returns a new matrix with the results rounded to 2 decimal places.

The function performs input validation to ensure:
- The matrix is a list of lists of integers or floats.
- Each row of the matrix has the same size.
- The divisor `div` is a number (either integer or float).
- The divisor `div` is not zero.

Exceptions raised:
- TypeError: If matrix is not a list of lists of integers/floats or if rows have different sizes, or if `div` is not a number.
- ZeroDivisionError: If `div` is zero.

Returns:
    A new matrix where each element is divided by `div` and rounded to 2 decimal places.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor and returns a new matrix with the result,
    rounded to 2 decimal places.

    Arguments:
    matrix -- A list of lists of integers or floats.
    div -- A number (integer or float) to divide each element of the matrix by.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats or if rows have different sizes.
    TypeError: If `div` is not a number.
    ZeroDivisionError: If `div` is zero.

    Returns:
    A new matrix where each element is divided by `div` and rounded to 2 decimal places.
    """
    # Validate that matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Validate that all elements of the matrix are integers or floats
    if not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Validate that all rows in the matrix are of the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Validate that div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Validate that div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round each result to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = [round(item / div, 2) for item in row]
        new_matrix.append(new_row)

    return new_matrix


#!/usr/bin/python3

"""
This module defines a function `matrix_divided` that divides each element of a matrix
by a given divisor, `div`, and returns a new matrix with the results rounded to 2 decimal places.

The function performs input validation to ensure:
- The input is a matrix (a list of lists of integers/floats).
- All rows of the matrix have the same size.
- The divisor `div` is a number (integer or float).
- The divisor `div` is not zero.

Exceptions raised:
- TypeError: If the input matrix is not a list of lists of integers/floats, or if the rows are not the same size, or if `div` is not a number.
- ZeroDivisionError: If `div` is zero.
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
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all elements in the matrix are integers or floats
    if not all(isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows have the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create the new matrix by dividing each element by div
    new_matrix = []
    for row in matrix:
        new_row = [round(item / div, 2) for item in row]
        new_matrix.append(new_row)

    return new_matrix


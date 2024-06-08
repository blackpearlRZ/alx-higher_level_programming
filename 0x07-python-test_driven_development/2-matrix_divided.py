#!/usr/bin/python3
"""
    A module that contains the matrix_divided function
"""


def matrix_divided(matrix, div):
    """
        A function that divides the a matrix by div

        Args:
            matrix: The matrix to divide
            div: The divisor

        Return:
            A new matrix containing the result of the division
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be an integer")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    result_matrix = []
    for list_x in matrix:
        list_tmp = []
        length = len(matrix[0])
        if type(list_x) is not list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if len(list_x) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in list_x:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            result = round((element / div), 2)
            list_tmp.append(result)
        result_matrix.append(list_tmp)
    return result_matrix

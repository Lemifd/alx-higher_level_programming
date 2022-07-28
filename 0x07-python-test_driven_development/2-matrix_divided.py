#!/usr/bin/python3
"""2-matrix_divided module"""


def matrix_divided(matrix, div):
    """matrix_divided function
    Divides each element of a matrix by an integer or float
    """
    size = len(matrix[0])
    mat = []
    mat_type_err = "matrix must be a matrix (list of lists) of integers/floats"
    for a_list in matrix:
        row_len = len(a_list)
        if size != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        row = []
        for num in a_list:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError(mat_type_err)
            if not isinstance(div, int) and not isinstance(div, float):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            a = round((num / div), 2)
            row.append(a)
        mat.append(row)
    return mat

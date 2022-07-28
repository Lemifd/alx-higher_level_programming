#!/usr/bin/python3
"""matrix_mul module"""


def matrix_mul(m_a, m_b):
    """matrix_mul docstring
    function multiplies two matrices
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(item_a, list) for item_a in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(item_b, list) for item_b in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(isinstance(val_a, int) or isinstance(val_a, float)
               for val_a in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(val_b, int) or isinstance(val_b, float)
               for val_b in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_list = []
    for row in range(len(m_b[0])):
        tmp_list = []
        for col in range(len(m_b)):
            tmp_list.append(m_b[col][row])
        inverted_list.append(tmp_list)

    matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_list:
            prod = 0
            for i in range(len(inverted_list[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        matrix.append(new_row)

    return matrix

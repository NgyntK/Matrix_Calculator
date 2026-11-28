from matrix.matrix import Matrix
from fraction.fraction import Fraction

def subtraction(A,B) :
    if not isinstance(A,Matrix) or not isinstance(B,Matrix) :
        raise TypeError("You need to provide matrices")
    if A.nb_lines != B.nb_lines or A.nb_columns != B.nb_columns :
        raise ValueError("The matrices must have the same dimensions.")

    result = Matrix.zero(A.nb_lines,A.nb_columns)

    for n in range(A.nb_lines) :
        for m in range(A.nb_columns) :
            result[n][m].data = (A.data[n][m]).sub(B.data[n][m])

    return result

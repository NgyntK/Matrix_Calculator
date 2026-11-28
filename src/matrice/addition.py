from matrice.matrix import Matrix
from fraction.fraction import Fraction

def addition(A,B) :
    if not isinstance(A,Matrix) or not isinstance(B,Matrix) :
        raise TypeError("You need to provide matrices")
    if A.nb_lines != B.nb_lines or A.nb_colomns != B.nb_colomns :
        raise ValueError("The matrices must have the same dimensions.")

    result = Matrix.zero(A.nb_lines,A.nb_colomns)

    for n in range(A.nb_lines) :
        for m in range(A.nb_colomns) :
            result[n][m] = A.data[n][m].add(B.data[n][m])

    return result

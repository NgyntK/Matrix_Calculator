from src.matrix import Matrix
from src.fraction import Fraction

def multiplication(A,B) :
    if not isinstance(A,Matrix) or not isinstance(B,Matrix) :
        raise TypeError("You need to provide matrices")
    if A.nb_colomns != B.nb_lines :
        raise ValueError("Matrices cannot be multiplied")

    result = Matrix.zero(A.nb_lines,B.nb_colomns)

    # TO DO

    return result

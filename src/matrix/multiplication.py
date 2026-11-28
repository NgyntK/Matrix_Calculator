from matrix.matrix import Matrix
from fraction.fraction import Fraction

def multiplication(A,B) :

    if not isinstance(A,Matrix,int) or not isinstance(B,Matrix,int) :
        raise TypeError("You need to provide matrices")

    if isinstance(A,int) or not isinstance(B,int) :
        return A*B

    if isinstance(A,int) and isinstance(B,Matrix) :
        result = Matrix.zero(B.nb_lines,B.nb_columns)
        for i in range(B.nb_lines):
            for j in range(B.nb_columns):
                result[i][j]= A*B[i][j]
        return result 

    if isinstance(B,int) and isinstance(A,Matrix) :
            result = Matrix.zero(A.nb_lines,A.nb_columns)
            for i in range(A.nb_lines):
                for j in range(A.nb_columns):
                    result[i][j]= B*A[i][j]
            return result 
    
    if A.nb_columns != B.nb_lines :
        raise ValueError("Matrices cannot be multiplied")

    result = Matrix.zero(A.nb_lines,B.nb_columns)
    
    for i in range(A.nb_lines) :
        for j in range(B.nb_columns) :

            sum = 0

            for u in range(A.nb_columns) :
                sum += A[i][u]*B[u][j]

            result[i][j] = sum

    return result
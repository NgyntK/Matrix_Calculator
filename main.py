# ==========================================
# Matrix_Calculator
# A Python project for matrix calculations
# ==========================================

from matrice.matrix import Matrix
from fraction.fraction import Fraction
from matrice.addition import addition

def main():
    print("================================")
    print("Welcome to Matrix_Calculator")
    print("================================")

    A = Matrix([[1,2],[3,4]])
    B = Matrix([[1, Fraction(1,2) ,3],[4,5,6]])
    C = Matrix.zero(4,2)
    D = Matrix.identity(3)

    matrices = {
        "A": A,
        "B": B,
        "C": C,
        "D": D
    }

    for letter, matrix_test in matrices.items():

        print(f"\nMatrice {letter} :")
        print(matrix_test)

        print("Nombre de lignes :", matrix_test.nb_lines)
        print("Nombre de colonnes :", matrix_test.nb_colomns)
        print("La matrice est-elle nulle ?", matrix_test.is_zero)
        print("La matrice est-elle vide ?", matrix_test.is_empty)
        print("La matrice est-elle carrée ?", matrix_test.is_square)
        print("La matrice est-elle identité ?", matrix_test.is_identity)

    E = addition(B,B)
    print(E)


if __name__ == "__main__":
    main()



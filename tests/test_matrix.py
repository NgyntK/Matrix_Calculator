from src.matrix.matrix import Matrix
from src.fraction.fraction import Fraction


def test_matrix_creation():
    A = Matrix([[1,2,3],[4,5,6]])
    assert A.data == [
                    [Fraction(1),Fraction(2),Fraction(3)],
                    [Fraction(4),Fraction(5),Fraction(6)]    
                ]



def test_matrix_shape():
    A = Matrix([[1,2,3],[4,5,6]])
    assert A.nb_lines == 2
    assert A.nb_columns == 3


def test_matrix_eq():
    A = Matrix([[1,2,3],[4,5,6]])
    B = Matrix([[1,2,3],[4,5,6]])
    assert A == B



def test_matrix_zero():
    A = Matrix.zero(2,4)
    B = Matrix.zero(2,2)
    assert A.data == [
                [Fraction(0),Fraction(0),Fraction(0),Fraction(0)],
                [Fraction(0),Fraction(0),Fraction(0),Fraction(0)]
                ]
    assert B.data == [
                [Fraction(0),Fraction(0)],
                [Fraction(0),Fraction(0)]
                ]

    assert A.is_zero
    assert B.is_zero



def test_matrix_identity():
    A = Matrix.identity(3)
    B = Matrix.identity(2)
    assert A.data == [
                [Fraction(1),Fraction(0),Fraction(0)],
                [Fraction(0),Fraction(1),Fraction(0)],
                [Fraction(0),Fraction(0),Fraction(1)]
                ]
    assert B.data == [
                [Fraction(1),Fraction(0)],
                [Fraction(0),Fraction(1)]
                ]

    assert A.is_identity
    assert B.is_identity

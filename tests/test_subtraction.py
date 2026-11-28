from src.matrix.matrix import Matrix
from src.fraction.fraction import Fraction
from src.matrix.subtraction import subtraction

def test_subtraction() :
    A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    B = Matrix([[5,5,3],[4,0,1],[7,2,3]])

    assert subtraction(A,B).data == [[6,7,6],[8,5,7],[14,10,12]]

    C = Matrix([[Fraction(1,2),2],[Fraction(7,3),7]])
    D = Matrix([[Fraction(1,2),5],[2,Fraction(5,4)]])
    E = Matrix([[0,-3],[Fraction(1,3),Fraction(23,4)]])


    assert subtraction(C,D) == E


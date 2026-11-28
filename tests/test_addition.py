from src.matrix.matrix import Matrix
from src.fraction.fraction import Fraction
from src.matrix.addition import addition

def test_addition() :
    A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    B = Matrix([[5,5,3],[4,0,1],[7,2,3]])

    assert addition(A,B).data == [
                            [Fraction(6),Fraction(7),Fraction(6)],
                            [Fraction(8),Fraction(5),Fraction(7)],
                            [Fraction(14),Fraction(10),Fraction(12)]
                            ]
    assert addition(A,B).data == [[6,7,6],[8,5,7],[14,10,12]]

    C = Matrix([[Fraction(1,2),2],[Fraction(7,3),7]])
    D = Matrix([[Fraction(1,2),5],[2,Fraction(5,4)]])


    assert addition(C,D).data == [
                            [Fraction(1), Fraction(7)],
                            [Fraction(13,3), Fraction(33,4)]
                            ]


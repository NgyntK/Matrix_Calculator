from src.fraction.fraction import Fraction


def test_fraction_creation():
    A = Fraction(2,3)
    assert A.numerator == 2
    assert A.denominator == 3

    B = Fraction(-5,10)
    assert B.numerator == -5
    assert B.denominator == 10



def test_fraction_eq() :
    A = Fraction(-5,10)
    B = Fraction(1,-2)
    assert A == B

    C = Fraction(0,10)
    D = Fraction(0,4)
    assert C == D

    E = Fraction(5,1)
    F = 5
    assert E == F

    G = Fraction(75,5)
    H = 15
    assert H == G



def test_fraction_simplify():
    A = Fraction(2,3).simplify()
    assert A.numerator == 2
    assert A.denominator == 3
    
    B = Fraction(-5,10).simplify()
    assert B.numerator == -1
    assert B.denominator == 2

    C = Fraction(0,10).simplify()
    assert C.numerator == 0
    assert C.denominator == 1

    D = Fraction(-5,-15).simplify()
    assert D.numerator == 1
    assert D.denominator == 3


def test_fraction_add():
    A = Fraction(2,3)
    B = Fraction(5,2)
    assert A.add(B) == Fraction(19,6)

    C = Fraction(2,3)
    D = Fraction(-5,3)
    assert C.add(D) == -1


def test_fraction_sub():
    A = Fraction(2,3)
    B = Fraction(5,2)
    assert A.sub(B) == Fraction(-11,6)
    
    C = Fraction(2,3)
    D = Fraction(-5,3)
    assert C.sub(D) == Fraction(7,3)


def test_fraction_mult():
    A = Fraction(2,3)
    B = Fraction(5,2)
    assert A.mult(B) == Fraction(5,3)

    C = Fraction(2,3)
    D = Fraction(-5,3)
    assert C.mult(D) == Fraction(-10,9)

    E = Fraction(7,-3)
    F = Fraction(-5,3)
    assert E.mult(F) == Fraction(35,9)



from fraction.fraction import Fraction


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
    assert A.__eq__(B)

    C = Fraction(0,10)
    D = Fraction(0,4)
    assert C.__eq__(D)


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



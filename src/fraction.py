#===============================================
# The coefficients of a matrix are not necessarily integers.
#===============================================

class fraction :
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator == 0 :
            raise ZeroDivisionError("denominator can't be zero")
        self.denominator = denominator

    def simplify(self) : # (a/b)
        a,b = self.numerator , self.denominator
        if b == 1 :
            return a

        elif a < 0 and b < 0 :
            return fraction(abs(a) , abs(b) )
        
        elif a > 0 and b < 0 :
            return fraction(-a , abs(b))

        elif self.gcd() == 1 :
            return self
        if self.gcd() != 1 :
            result = fraction(a//self.gcd() , b//self.gcd() )
            if result.denominator == 1 :
                return result.numerator
            return result

    def gcd(self):
        a,b = self.numerator , self.denominator
        if isinstance(a,int) and isinstance(b,int) :
            while b != 0:
                a,b = b, a%b
            return abs(a)

    def __add__(self,other) : 
        a,b = self.numerator , self.denominator
        if isinstance(other,int) : # (a/b)+c= (a+cb)/b
            result = fraction(a + other * b , b )

        if isinstance(other, fraction) : # (a/b)+(c/d) = (a+c)/b si b=d
            c,d = other.numerator , other.denominator
            if b == d :
                result = fraction( a+c , b )

            else : # (a/b)+(c/d) = (ad+cb)/bd si b!=d
                result = fraction( a*d + c*b , b*d )
        return result.simplify()

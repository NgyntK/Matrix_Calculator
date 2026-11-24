#===============================================
# The coefficients of a matrix are fractions. 
#The `Fraction` class will then be responsible for all arithmetic operations, 
# while the `Matrix` class can focus exclusively on matrix operations.
#===============================================

class fraction :

    def __init__(self, numerator, denominator = None ):

        """
        Initialize a fraction with a numerator and a denominator.
        The numerator and denominator must be integers.
        If no denominator is provided, it defaults to 1.
        A denominator equal to zero is not allowed.
        """

        if not isinstance(numerator, int) or (denominator is not None and not isinstance(denominator, int)):
            raise TypeError("Numerator and denominator must be integers")
        self.numerator = numerator

        if denominator is None :
            denominator = 1

        if denominator == 0 :
            raise ZeroDivisionError("denominator can't be zero")
        
        self.denominator = denominator

    def simplify(self) : # (a/b)

        """
        Return the fraction in its simplest form.

        The greatest common divisor (GCD) of the numerator
        and denominator is used to reduce the fraction.

        The denominator is always kept positive.
        If the fraction is already simplified, return itself.
        """

        a,b = self.numerator , self.denominator

        if a < 0 and b < 0 : # (-a/-b) = a/b
            a,b = abs(a) , abs(b)
            return fraction(a,b).simplify()
        
        elif a > 0 and b < 0 : # By convention, the “-” is placed in the numerator
            a,b = -a , abs(b)
            return fraction(a,b).simplify()

        elif self.gcd() == 1 : # the fraction cannot be simplified
            return self
        
        if self.gcd() != 1 : # the fraction can be simplified
            return fraction(a//self.gcd() , b//self.gcd() )


    def gcd(self): 

        """
        Calculate the greatest common divisor (GCD)
        of the numerator and denominator for simplify the fraction.

        gcd(a,b) = gcd(b,a) = gcd(a,b-a) = gcd(-a,b) = gcd(a,-b) = gcd(-a,-b)
        """

        a, b = abs(self.numerator), abs(self.denominator)

        if a == 0:
            return b
        if b == 0 or a == b:
            return a
        if a > b:
            a, b = b, a

        return fraction(a, b-a).gcd()

    def add(self,other) : 

        """
        Add two fractions.
        """

        if not (isinstance(self , fraction) and isinstance(other,fraction)) :
            raise TypeError("variables must be fractions")
        a,b = self.numerator , self.denominator
        c,d = other.numerator , other.denominator
        
        return fraction( a*d + c*b , b*d ).simplify()


    def __repr__(self):
        
        """
        Return the fraction as a string.

        If the denominator is equal to 1, the fraction is
        represented as an integer. Otherwise, it is represented
        in the form numerator/denominator.
        """
        
        if self.denominator == 1 :
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

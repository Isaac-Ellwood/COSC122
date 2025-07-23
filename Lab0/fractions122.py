class Fraction():
    '''Defines a Fraction type that has an integer numerator and a non-zero integer denominator'''

    def __init__(self, num=0, denom=1):
        ''' Creates a new Fraction with numerator num and denominator denom'''
        if isinstance(num, int) and isinstance(denom, int):
            self.numerator = num
            if denom != 0:
                self.denominator = denom
            else:
                raise ZeroDivisionError
        else:
            raise ValueError('Numerator and denominator must be ints')
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"
    
    def __add__(self,other):
        numerator = (self.numerator * other.denominator ) + (other.numerator * self.denominator)
        denominator = self.denominator * other.denominator
        return Fraction(numerator,denominator)
    
    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator,denominator)

    def __eq__(self, other):
        #a/b == c/d if a*d == b*c
        if (self.numerator*other.denominator == self.denominator*other.numerator):
            return True
        return False

class ReducedFraction(Fraction):                  # is a sub-class of the Fraction class
    """Reduced Frac"""
    def __init__(self, numerator, denominator=1):
        super().__init__(numerator, denominator)  # use Fraction.__init__ 
        self._reduce()                            # next, reduce the numerator/denominator 
    
    def __repr__(self):
        return f"ReducedFraction({self.numerator}, {self.denominator})"


    def _reduce(self):
        """ Reduces the fraction to its simplest possible form.
        NOTE: This method does NOT return anything, 
              it updates self.numerator and self.denominator
        """
        ###TO DO:###
        # Put your code here to reduce the fraction using the greatest common divisor
        # That is call the find_gcd function and use the result to update
        # self.numerator and self.denominator
        gcd = self.find_gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator/gcd)
        self.denominator = int(self.denominator/gcd)

    def find_gcd(self, num1, num2):
        """ 
        Returns the Greatest Common Divisor (GCD) of num1 and num2. 
        Assumes num1 and num2 are positive integers. 
        """
        smaller = min(num1, num2)
        for i in range(smaller, 1, -1):
            if num1 % i == 0 and num2 % i == 0:
                return i
        return 1
    
    def __add__(self, other):
        fraction_result = super().__add__(other)   # uses the __add__ method from Fraction
        reduced_result = ReducedFraction(fraction_result.numerator,fraction_result.denominator)
        return reduced_result

    def __mul__(self, other):
        fraction_result = super().__mul__(other)
        reduced_result = ReducedFraction(fraction_result.numerator,fraction_result.denominator)
        return reduced_result

class MixedNumber():
    def __init__(self, number, fraction):
        # Ensure fraction is reduced
        fraction = ReducedFraction(fraction.numerator, fraction.denominator)

        # Extract the whole part from the fraction if it's improper
        extra_whole = fraction.numerator // fraction.denominator
        self.number = number + extra_whole

        # Get the new numerator (remainder part only)
        fraction.numerator = fraction.numerator % fraction.denominator
        self.fraction = fraction
    
    def __repr__(self):
        f"MixedNumber({self.number}, ReducedFraction({self.fraction.numerator}, {self.fraction.denominator}))"

    def __str__ (self):
        return f"{self.number} and {self.fraction.numerator}/{self.fraction.denominator}"
    
    def __add__ (self,other):
        number_result = self.number + other.number
        fraction_result = self.fraction + other.fraction
        return MixedNumber(number_result, fraction_result)
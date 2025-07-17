from fractions122 import Fraction    # You must import your fraction class before using it
f = Fraction()          # Creates a fraction with the default values (numerator 0, denominator 1)
f.numerator             # Attributes of classes can be accessed using '.' notation like methods
f.denominator
f                  # Returns a weird looking string which describes the memory location of the object
g = Fraction(1, 2)  # Creates a fraction numerator = 1, denominator = 2 (1/2)
print(f"Numerator is {g.numerator} and denom is {g.denominator}")
print(g)
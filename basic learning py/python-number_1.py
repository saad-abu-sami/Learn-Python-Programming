from decimal import Decimal as D
print(D('1.1') + D('2.2'))
print(D('1.2') * D('2.50'))
#Python provides operations involving fractional numbers through its (fractions) module.
import fractions
print(fractions.Fraction(1.5))
print(fractions.Fraction(2.5))
#Fortunately, Fraction allows us to instantiate with string as well.
print(fractions.Fraction('1.3'))
from fractions import Fraction as F
print(F('1.3')+F('1.3'))
print(1/F(1.5))
print(F(-3.0)>0)
print(F(-3.0)<0)

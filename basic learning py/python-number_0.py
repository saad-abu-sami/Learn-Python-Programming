print(type(5)) #there are three types of number in python 1.integer
print(type(5.00)) #2. floating point
c = 5 + 3j  #3. complex number
print(isinstance(c, complex))
#convert programming number binary,octal,hexadecimal to decimal
print(0b1101011) #convert binary to decimal
print(0xABCDEF) #covert hexadecimal to decimal
print(0o15) #convert octal to decimal
#We can also use built-in functions to convert between types explicitly.
print(int(-2.3)) #print only the integer part with symbol like subtraction
print(float(5)) #print only float position type .00
print(complex('3+5j')) #These functions can even convert from strings.
import decimal
print(0.1)
print(decimal.Decimal(0.1)) #floating-point numbers have precision up to 15 decimal places

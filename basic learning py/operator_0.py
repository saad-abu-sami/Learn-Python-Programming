a = 10
b = 3
c = a > 3 and b > 2  # both are correct
d = a < 3 or b > 2  # one is correct
print(a / b) ; print(a % b)  # reminder
print(type(9.9+1.1)) #its float coz 9.9 plus 1.1 equal 11.0
print(a ** b)  # math power (10^3)
print(a // b)  # integer vagfol
print(2 // 4) #it returns zero 0, because this actually retured an int rounded down.
print(a > b)  # true vs false
print(c);print(d)
a += 2 ; print(a)
r = 'bangladesh' ; t = 'desh'
print(t in r) ; print(r in t) #desh in bangladesh,thats why that is true
u = 'bangladesh' ; v = 12 #two identity operator in python (is,is not)
print(u is v) ; print(u is not v) #u=bangladesh have 8 string where we tell it 12 false
'''we see that x1 and y1 are integers of the same values, so they are equal as well as identical. '''
x1 = 5 ; y1 = 5; print(x1 is y1) #TRUE
'''The largest number you can represent with 8 bits is 255 in decimal notation.
 So for numbers greater than 255 different memory locations are set, so they are not equal'''
x2 = 6000 ; y2 = 6000 ; print(x2 is not y2) #TRUE
'''Same(x1,y1) is the case with x3 and y3 (strings). So they are equal'''
x3 = 'Hello' ; y3 = 'Hello' ; print(x3 is y3) #TRUE
'''But x4 and y4 are lists. They are equal but not identical. 
It is because the interpreter locates them separately in memory although they are equal'''
x4 = [1,2,3] ; y4 = [1,2,3] ; print(x4 is not y4) #TRUE


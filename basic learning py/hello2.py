colors = ['red',
          'blue',
          'green']
print(colors)
a = 1 ; b = 2 ; c = 3 ; x = 78.3456789
print(a);print(b);print(c)
print('The value of x is %3.2f' %x) #The value of x is 12.35
print('The value of x is %3.4f' %x) #The value of x is 12.3457
print(int('10'))
print(float('10')) #here we make a int to float using float.
# Escape Sequence in Python
weather = 'It\'s \"kind of\" sunny.' #we cant use triple quot, apstopi's, in a single line. so we use \slash
print(weather)
import sys
print(sys.path) #Python looks at several places defined in [sys.path]
print('The value of a is',a) #it prints var a value
print('The value of b is {} and c is {}'.format(b,c)) #we would like to format our output
print('I love {0} and {1}'.format('bread','butter')) #to make it look attractive by using [str.format()]
print('I love {1} and {0}'.format('bread','butter')) #This method is visible to any string object.
print('Hello {name}, {greeting}'.format(greeting='Goodmorning', name='John'))
print(1,2,3,4, sep='*') #here sep use the star in every number
print(1,2,3,4, sep='#', end='&' ) #and here end using for using the and & or any key in last



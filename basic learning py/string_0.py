a = ' data science '
print(a[1]) #strings in Python are arrays of bytes representing unicode characters.
print(a[2:5]) #font 0,1=d,a then t,a,space
print(a[-7:-4]) #from end e,c,n,e, -4 then sci -7
print(len(a))
print(a.strip()) #no space on terminal [data science].The strip() method removes any whitespace from the beginning or the end
print(a.upper()) #all capital letter
print(a.lower()) #all small letter
print(a.replace(' data','Python string')) #to replace the word data
print(a.split()) #to divide a pherese or sentense to all word
b= 'a am a student'
print(b.split())
print('My favourite topic is %s' %a) #1 way to print strng
print('My favourite topic is',a) #2 way to print strng
print('My favourite topic is %s' %(a)) #3 way to print strng
m = input()
n = input() #input string can e declared
print('My favourite language are: ',m, 'and',n ) #1 way to declare
number = 234.497462590
print('%.4f' %number)
message_double_cote = """
Hi John,
This is SAMI from PSTU
Blah blah blah
"""
print(message_double_cote) #multi line type messege with double qutetion
message_single_cote = '''
Hi John,
This is SAMI from PSTU
Blah blah blah
'''
print(message_single_cote) #multi line type messege with single qutetion





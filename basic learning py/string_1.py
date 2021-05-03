x = 'Dhaka'
y = 'Khulna'
z = 'Sylhet'
Built = 1886
print('-'.join((x, y, z))) #to join word or sentense
print(z.swapcase()) #to upper letter to lower and low to up
print(x.count('a')) #to count same letter how many times used in a word
m = 'python'
print(m.capitalize()) #to capittal a word or sentense
print(m.casefold()) #like the lower function
n = 'bangladesh is my motherland. i just love her!'
print(n.title()) #to capital all the word in a sentense
print(n.strip('!'))  #to delet the previous symbol('!') using strip
sentence = 'How can a clam cram in a clean cream can?' #count funcyion is very smart
print(sentence.count('c')) #counting all the c in sentence that is 6
print(sentence.count('c',5)) #counting c from index 5[how_c] to last that is 5
print(sentence.count('c',5,9)) #counting c from index 5[how_c] to 9[a_clam......], so there is no c
print(sentence.count('a',5,10)) #there is 2 a , now be understand
print(sentence.find('c')) #here answer is 4 !!!
"""But we are supposed to get several outputs. So where is the mistake? Not actually wrong. The function of this 
function is to first find the desired character in the index that will show as the output or return to us."""
print(sentence.find('c',5))
"""Well, I got a c in the index number 4. Now let's start the search again from number 5.
 In the 2nd c we got the number 10 index."""
#Formatted string
print(f'Sami, Hi. Do you know {y} is built in {Built}') #Look again here f is mandatory
#we can do the same things in another way
print('{}, Hi. Do you know {} is built in {}'.format('Sami','KHULNA','1886'))
print(y + 'ya') #Python immu tability 


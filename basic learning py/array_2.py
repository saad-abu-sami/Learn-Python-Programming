import array as arr

odd = arr.array('i', [1, 3, 5])
even = arr.array('i', [2, 4, 6])
numbers = arr.array('i')   # creating empty array of integer
numbers = odd + even
print(numbers)

import array as arr

numbers = arr.array('i', [10, 11, 12, 12, 13])
print(numbers.pop(2))   # Output: 12 remove this one
print(numbers)   # Output: array('i', [10, 11, 13])

import array as arr
a = arr.array('i', [2, 4, 6, 8])
print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-2]) #last to (8-- done ) after 6

import array as arr
numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)
print(numbers_array[2:5]) # 3rd to 5th
print(numbers_array[:-5]) #  last to -5 (5,48,52,42,5-- 5done) after 62
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])   # beginning to end
numbers_list[2:5] = arr.array('i',[4,6,8]) #change many new int from n[2] to n[5]
print(numbers_list)
numbers_list[0] = 0 #change single new int n[0]
print(numbers_list)
numbers_list.extend([99,69]) #include more integer using extend
print(numbers_list)
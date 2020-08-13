import array as arr

numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)

print(numbers_array[2:5]) 
print(numbers_array[:-5]) 
print(numbers_array[5:])  
print(numbers_array[:])   

import array as arr

numbers = arr.array('i', [1, 2, 3, 5, 7, 10])
numbers[0] = 0    
print(numbers) 
numbers[2:5] = arr.array('i', [4, 6, 8])   
print(numbers)
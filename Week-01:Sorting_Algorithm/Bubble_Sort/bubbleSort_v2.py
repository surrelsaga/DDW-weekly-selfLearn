# Optimize bubble sort 

# main idea is in the outer iteration
# if the sequence is correctly in order then no need to iterate anymore
# sign to stop: sequence in order <-> no swap is made <-> assign a variable to keep track of this

# My pseudocode
# Bubble sort
# Version 2
# Input: array
# Output: none, sort in place
# Steps:
# 1. n: array length
# 2. for outer_index from 1 to n-1:
#     2.1 haveSwapped = False to track if there's a swap inside the array
#     2.2 for inner_index from 1 to n-1:
#         2.2.1 firstNumber = array[innner_index - 1]
#         2.2.2 secondNumber = array[inner_index]
#         2.2.3 if firstNumber > secondNumber:
#             array[inner_index - 1], array[inner_index] = array[inner_index], array[inner_index - 1]
#             haveSwapped = True 
            
#     2.3 if no swap is made, the array is already in order then break

arr = [16, 1, 2, 3, 4, 5]
print(arr)

n = len(arr)
for outer_index in range(1, n):
    haveSwapped = False
    for inner_index in range(1, n):
        firstNumber = arr[inner_index - 1]
        secondNumber = arr[inner_index]
        if firstNumber > secondNumber:
            arr[inner_index - 1], arr[inner_index] = arr[inner_index], arr[inner_index - 1] 
            haveSwapped = True
    
    if (haveSwapped == False):
        break

print(arr)

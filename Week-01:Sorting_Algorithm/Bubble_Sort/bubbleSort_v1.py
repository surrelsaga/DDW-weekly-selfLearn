# My Pseudocode

# Declare the list here 
# outer iterations (n - 1 iterations): for loop for n - 1 times, each time we execute the inner iteration
# inner iterations: for loop through the list, compare list[i] vs list[i + 1] and do a swap if left > right

# Course pseudocode

# Bubble sort
# Version: 1
# Input: array
# Output: None, sort in place
# Steps:
# 1. get n = array length
# 2. For outer_index from 1 to n -1, do:
#     2.1 For inner_index from 1 to n -1, do:
#         2.1.1 declare firstNumber = array[inner_index - 1]
#         2.1.2 declare secondNumber = array[inner_index]
#         2.1.3 if first_number > second_number, do:
            #  2.1.3.1 swap(firstNumber, secondNumber)
            
# Code here
arr = [16, 14, 10, 8, 7, 8, 3, 2, 4, 1]
print(arr)

n = len(arr)
for outer_index in range(1, n):
    for inner_index in range(1, n):
        firstNumber = arr[inner_index - 1]
        secondNumber = arr[inner_index]
        
        if( firstNumber > secondNumber ):
            # swap
            arr[inner_index - 1], arr[inner_index] = arr[inner_index], arr[inner_index - 1]
            
print(arr)

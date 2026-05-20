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

# arr = [16, 1, 2, 3, 4, 5]
# print(arr)

# n = len(arr)
# for outer_index in range(1, n):
#     haveSwapped = False
#     for inner_index in range(1, n):
#         firstNumber = arr[inner_index - 1]
#         secondNumber = arr[inner_index]
#         if firstNumber > secondNumber:
#             arr[inner_index - 1], arr[inner_index] = arr[inner_index], arr[inner_index - 1] 
#             haveSwapped = True
    
#     if (haveSwapped == False):
#         break

# print(arr)

# The idea above is slightly redundant
# the outer loop is not running for (n - 1) times to place numbers in their correct positions
# the outer loops is supposed to run less, as long as there is no swap
# we will know that the list is already in order, we just stop the loop
# we don't know the exact numbers of iterations and we know the condition to stop -> while loop sign

# MAIN IDEA is to keep looking for swap after one outer iteration (which moved the nth largest num to its correct position)

arr = [20, 6, 7, 4, 15, 21, 34, 11, 5]
print(arr)

n = len(arr)
swapped = True
while( swapped == True ):
    swapped = False
    for inner_index in range(1, n):
        firstNumber = arr[inner_index - 1]
        secondNumber = arr[inner_index]
        if firstNumber > secondNumber:
            arr[inner_index - 1], arr[inner_index] = arr[inner_index], arr[inner_index - 1] 
            swapped = True

print(arr)

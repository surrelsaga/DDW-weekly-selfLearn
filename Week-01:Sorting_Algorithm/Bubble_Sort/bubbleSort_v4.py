# In v3, we know that the nth largest number is placed in its correct position after the nth iteration
# That's why we reduce the inner iteration by 1
# But what if in one outer iteration pass, there are more than one number are in their correct positions
# then in that case, inner iteration reduced by one means still swap until that position
# which is not optimized

# Thought process: how do we know which position to swap until
# Actually, when the swap stopped, it actually means the number is put in its correct position
# In the next outer iteration, we just need to compare and swap until the position where the swap
# was stopped. That is enough already

# test cases: [16, 10, 2, 8, 10]
# 1st outer iteration: need 4 inner iterations to make [10, 2, 8, 10, 16]. Lastest swap is at 5th element
# 2nd outer iteration: need 2 inner iterations only to make [2, 8, 10, 10, 16]. Lastest swap is at 3rd element


# My pseudocode
# Steps:
# 1. n: array length

# 2.latestSwapPosition = n - 1 -> position of the latest swap (a copy of n)
# but at first, we still need to swap until the very end for the largest number

# 3. for outer_index from 1 to n-1:
#     3.1 haveSwapped = False (optimization from v2)
#     3.2 for inner_index from 1 to latestSwapPosition:
#       3.3.1 firstNumber = array[inner_index - 1]
#       3.3.2 secondNumber = array[inner_index]
            
#       3.3.3  if firstNumber > secondNumber:
#         3.3.3.1 swap(firstNumber, secondNumber)
#         3.3.3.2 haveSwapped = True # optmization from v2
#         3.3.3.3 latestSwapPosition = inner_index
    
#     3.3 Optimization from v2
#         if haveSwapped == False -> break (the outer loop)

arr = [16, 14, 10, 8, 7, 8, 3, 2, 4, 1]
n = len(arr)
latestSwapPosition = n - 1

print(arr)

for outer_index in range(1, n):
    haveSwapped = False;
    for inner_index in range(1, latestSwapPosition + 1):
        firstNumber = arr[inner_index - 1]
        secondNumber = arr[inner_index]
        
        if firstNumber > secondNumber:
            arr[inner_index - 1], arr[inner_index] = arr[inner_index], arr[inner_index - 1]
            haveSwapped = True
            latestSwapPosition = inner_index
            
    if (haveSwapped == False): 
        break
    
print(arr)

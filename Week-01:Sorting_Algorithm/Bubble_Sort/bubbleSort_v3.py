# Optimize: 
# - In first outer iteration, the largest number will be placed in its correct position (e.g: largest to rightmost)
# - In the next outer iteration. Since the largest number is already in its position. The inner interations can be reduced by one

# -> Question: Can the outer iteration also be reduced by one? The answer is no (not due to this optimization but due to the v2 optimization)
# Since each outer iteration (nth) means the nth largest number is moved to its correct position, since we have n numbers -> still need n - 1 iterations


# My pseudocode
# Steps:
# 1. n: array length
# 2.inner_iteration = n - 1 -> number of inner iterations (a copy of n)
# 3. for outer_index from 1 to n-1:
#     3.1 haveSwapped = False (optimization from v2)
#     3.2 for inner_index from 1 to inner_iteration:
#       3.3.1 firstNumber = array[inner_index - 1]
#       3.3.2 secondNumber = array[inner_index]
            
#       3.3.3  if firstNumber > secondNumber:
#         3.3.3.1 swap(firstNumber, secondNumber)
#         3.3.3.2 haveSwapped = True # optmization from v2
                
#     3.3 Reduce inner iteration after one outer iteration
#         inner_iteration = inner_iteration - 1
        
#     3.4 Optimization from v2
#         if haveSwapped == False -> break (the outer loop)

arr = [16, 14, 10, 8, 7, 8, 3, 2, 4, 1]
n = len(arr)
inner_iteration = n - 1

print(arr)

for outer_index in range(1, n):
    haveSwapped = False;
    for inner_index in range(1, inner_iteration + 1):
        firstNumber = arr[inner_index - 1]
        secondNumber = arr[inner_index]
        
        if firstNumber > secondNumber:
            arr[inner_index - 1], arr[inner_index] = arr[inner_index], arr[inner_index - 1]
            haveSwapped = True
            
    if (haveSwapped == False): 
        break        
    inner_iteration -= 1
    
print(arr)
    




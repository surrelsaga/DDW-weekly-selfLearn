# Input: Array or list of numbers
# Output: the Sum of the array
# Steps:
# 1. if the number of element is one only
#     1.1 Return that element as the sum of the array
# 2. Otherwise,
#     2.1 Return the addition of the first element with the sum of the rest of the array

arr = [1,0, 2, 4, 5]

def sumArray_v1(array):
    if len(array) == 1:
        return array[0]
    
    return array[0] + sumArray_v1(array[1:])

print( sumArray_v1(arr) )

# The above solution is good but it kinda wastes memory because everytime, we slice the array
# we are creating a new copy of the array

# Better recursive solution. This one will measure sum starting from a desired index
# we want to perform recursion on the rest of the array, then we change approach:
# we don't slice the array anymore but now keep track of the index to return the sum
def sumArray_v2(array, index = 0):
    if array[index] == len(array) - 1:
        return array[index]
    
    return array[index] + sumArray_v2(array, index +1)

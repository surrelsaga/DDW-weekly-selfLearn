# PCDIT
# Problem statement: given a sequence of numbers, write steps to sort the sequence in some orders

# TEST CASES (inside the doc)
# [5, 2, 9, 1, 6]
# start from second element
# compare w the left element -> swap -> [2, 5, 9, 1, 6]
# move to 3rd element
#  compare w left element -> no swap -> [2, 5, 9, 1, 6]
# move to 4th element
#  compare w left element -> swap -> [2, 5, 1, 9, 6]
#                       continue swap -> [2, 1, 5, 9, 6]
#                       continue swap -> [1, 2, 5, 9, 6]
# move to 5th element -> swap and swap until we get [1, 2, 5, 6, 9]

# idea is like we try to INSERT a number to its correct position as we meet that number when we traverse thru the array
# correct position here meaning the correct position in the sorted array after each iteration to pick nth element
# e.g above: 1 is moved to the left most since it's its correct position in the sorted array [2, 5, 1, 9 , 6]

# design of algo
# 1. outer iteration: we run from 2nd element to the last element (nth) -> n - 1 iterations
# 2. inner iteartion: not fixed since it may move to leftmost or to its correct position in the sorted array
# support for 2: if it moves leftmost, suppose its position is i then we need i iterations to swap
#                if it moves to its supposedly correct position, it's less than i
# a non-fixed loop is a sign for while loop

# PSEUDOCODE
# 1. n: array length
# 2. for outer_index from 1 to n - 1:
#       inner_index = outer_index (start from the second element)
#       As long as (inner_index > 0) and (array[inner_index] < array[inner_index - 1]): the choosen element is smaller then its left neighbor
#          swap array[inner_index] and array[inner_index - 1]
#          inner_index -= 1 since we move backwards to continue comparing and swapping

# IMPLEMENTATION AND TEST
arr = [5, 2, 9, 1, 6]
n = len(arr)

print(arr)

for outer_index in range(1, n):
    inner_index = outer_index
    while( (inner_index > 0) and (arr[inner_index] < arr[inner_index - 1]) ):
        # swap
        arr[inner_index], arr[inner_index - 1] = arr[inner_index - 1], arr[inner_index]
        # move one step back to compare the choosen element
        inner_index -= 1

print(arr)

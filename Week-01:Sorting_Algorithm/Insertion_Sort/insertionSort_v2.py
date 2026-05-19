# Optimised

# Test case see in doc
# [5, 2, 1, 9, 6]
# Overall idea: (see the visualisation)
# It's like we take the choosen element outside, store in a variable
# we then compare with the left neighbor
# if the left neighbor is larger, it can go through the space that was left by the choosen element
# we then move backward, compare the choose element with the second left neighbor
# if it's still larger, it can go through
# we do that until we find a position that the choose element is larger than the neighbor
# that neighbor can not go through and we will INSERT our choose element in that position

# PSEUDOCODE
# 1.for outer_index from 1 to n-1:
#    1.1inner_index = outer_index (start from second element)
#    1.2 numberToTakeOut = array[inner_index] (take out and store the choosen element)
#    1.3 As long as( inner_index > 0 and numberToTakeOut < array[inner_index - 1] ):
#        1.3.1 array[inner_index] = array[inner_index - 1] (we move the verified neighbor to the empty spot)
#        1.3.2 inner_index -= 1 (move back by 1 to compare with the next left neighbor)
#    When the loop terminates, the inner_index is the position that we should insert the choose number in
#    1.4 array[inner_index] = numberToTakeOut

# IMPLEMENTATION AND TEST
arr = [5, 2, 9, 1, 6]
n = len(arr)

print(arr)

for outer_index in range(1, n):
    inner_index = outer_index
    numberToTakeOut = arr[inner_index]
    while( (inner_index > 0) and (numberToTakeOut < arr[inner_index - 1]) ):
        # move the neighbor forward by 1
        arr[inner_index] = arr[inner_index - 1]
        # move one step back to compare the choosen element with the next left neighbor
        inner_index -= 1
    # Insert the number in its correct position
    arr[inner_index] = numberToTakeOut

print(arr)

# PCDIT

# Problem statement: given an arbitrary array and sort it in ascending order

# Design of algo:
# Basic idea:
# First recursively divide the array in half until all the children arrays only have 1 element
# Since every children is sorted, we will MERGE them together

# MERGE involves: 2 pointers, pointing to the left most of the 2 arrays that we gonna merge
# whichever is smaller will be placed first in the merged array


# IMPLEMENTATION (recursion):
# Base case: when all children arrays have only 1 element
# Recursive case:
# When number of arrays > 1, we split the array in 2 recursively
# we start sorting the array first before we merge

# pseudo:

# BREAK THE PROBLEMS DOWN: we need 2 different operations: merge and mergeSort

# Merge Sort
# Input:
#  - array = sequence of integers
#  - p = index of beginning of array
#  - r = index of end of array
# Output: None, sort the array in place
# Steps:
# 1. if r - p > 0, do:
#     1.1 calculate q = (p + r) / 2
#     1.2 call MergeSort(array, p, q)
#     1.3 call MergeSort(array, q+1, r)
#     1.4 call Merge(array, p, q, r)


# Merge

# We have one array, we split in half => then we sort each splited arrays, then merge them

# Input:
# - array = sequence of integers
# - p = beginning index of left array, which is also the beginning of the input sequence
# - q = ending index of left array
# - r = ending index of right array
#   Output: None, sort the array in place
#   Steps:

# 1. nleft = q - p +1
# 2. nright = r - q
# 3. left_array = array[p...q]
# 4. right_array = array[(q+1)...r]
# 5. left = 0
# 6. right = 0
# 7. dest = p
# 8. As long as (left < nleft) AND (right < nright), do:
#    8.1 if left_array[left] <= right_array[right], do:
#    8.1.1 array[dest] = left_array[left]
#    8.1.2 left = left + 1
#    8.2 otherwise, do:
#    8.2.1 array[dest] = right_array[right]
#    8.2.2 right = right + 1
#    8.3 dest = dest + 1
# 9. As long as (left < nleft), do:
#    9.1 array[dest] = left_array[left]
#    9.2 left = left + 1
#    9.3 dest = dest + 1
# 10. As long as (right < nright), do:
#     9.1 array[dest] = right_array[right]
#     9.2 right = right + 1
#     9.3 dest = dest + 1



def merge(array, p, q, r):
    nleft = q - p + 1
    nright = r - q
    left_array = array[p: (q+1)]
    right_array = array[(q + 1): (r + 1)]
    left = 0
    right = 0
    dest = p
    
    # 2 pointers point to index in left and right array
    while left < nleft and right < nright:
        if left_array[left] <= right_array[right]:
            array[dest] = left_array[left]
            left += 1
        else:
            array[dest] = right_array[right]
            right += 1
        
        dest += 1
    
    # right array is exhauted, we only point to index in left array
    while left < nleft:
        array[dest] = left_array[left]
        left += 1
        dest += 1
        
    # left array is exhauted, we only point to index in right array
    while right < nright:
        array[dest] = right_array[right]
        right += 1
        dest += 1


def mergeSort(array, p, r):
    if r - p > 0:
        q = (p + r) // 2
        mergeSort(array, p, q)
        mergeSort(array, q+1, r)
        merge(array, p, q, r)


arr = [6, 7, 9, 10, 4, 7, 3, 6, 9, 12]

mergeSort(arr, 0, len(arr) - 1)

print(arr)

# PCDIT

# Problem statement:
# Input: array of integers
# Output: None
# Process: Sort the elements of the array in place using heapsort

# Test cases: (see in doc)
# basic idea: we turn the array into heap, implement max-heapify on it
# 100% the largest element will be in the root node
# we take this largest element, swap it with the last element in the array
# then we continue the max-heapify with the remaining elements in the array to find the largest
# we iterate until we get a array sorted in ascending order.
# => 1 

# Design of algo:
# def heapsort(array):
# Input:
#   - array: any arbitrary array
# Output: None
# Steps:
# 1. call build-max-heap(array)
# 2. heap_end_pos = length of array - 1 # index of the last element in the heap
# 3. As long as (heap_end_pos > 0), do:
#     3.1 swap( array[0], array[heap_end_pos])
#     3.2 heap_end_pos = heap_end_pos -1 # reduce heap size
#     3.3 call max-heapify(array[from index 0 to heap_end_pos inclusive], 0)


# IMPLEMENTATION
arr = [1, 2, 8, 7, 14, 9, 3, 10, 4, 16]
print(arr)

# find index of left child of the current node
def left(index):
    # Input: index of current node
    # Output: index of the left child node
    # Steps: 
    # 1. return 2 * index + 1
    return 2 * index + 1

# find index of right child of the current node
def right(index):
    # Input: index of current node
    # Output: index of the right child node
    # Steps:
    # 1. return (index + 1) * 2
    return (index + 1) * 2

# Modify so it syncs with our idea. Cause we still keep the same array
# But we only want to build-max-heap until some points inside the array 
# (technically imagine it like a new array with less elements)
# so neede to compare till heap_end
# => heap_end defines the exclusive boundary of the active heap
# the heap occupies indices [0, heap_end]
def max_heapify(arr, indexOfCurrentNode, heap_end_pos):
    current_i = indexOfCurrentNode #start from index of current node (input)
    
    while( left(current_i) < heap_end_pos ): #ensure that the current node have children
        left_i = left(current_i)
        right_i = right(current_i)
        
        # In case where it only has one child (left) then the largest child element is the left
        if( right(current_i) >= heap_end_pos ):
            max_child_i = left_i
        else:
            # Finding the index of the larget child node element
            if( arr[left_i] >= arr[right_i] ):
                max_child_i = left_i
            else:
                max_child_i = right_i
        
        # if the child node element larger than current node element, swap (push the node element down)
        if arr[max_child_i] > arr[current_i]:
            arr[max_child_i], arr[current_i] = arr[current_i], arr[max_child_i]
        else:
            break
            
        # move to the position (index of the larger child node) to continue analyzing
        current_i = max_child_i
     

# Modify the build-max-heap so that it can work on the remaining unsorted elements of the array
# Because we already swap the largest element with the last element in the array
# just need to build_max_heap to find the next largest and continue swapping
# => heap_end defines the exclusive boundary of the active heap
# the heap occupies indices [0, heap_end]
def build_max_heap(arr, heap_end_pos):
    # previously the heap_end here is n (len(arr))
    starting_index = (heap_end_pos // 2) - 1
    
    for current_index in range(starting_index, -1, -1):
        max_heapify(arr, current_index, heap_end_pos)
        
        
def heapSort(arr):
    n = len(arr)
    build_max_heap(arr, n) #find largest from 0 to n - 1
    heap_end_pos = n - 1 #first swap to the latest element
    
    while( heap_end_pos > 0 ):
        arr[0], arr[heap_end_pos] = arr[heap_end_pos], arr[0]
        # the new latest element position is moved backward by 1 (the previous last element is the largest alr)
        heap_end_pos -= 1
        
        # continue build-max-heap to find next largest element
        # '+1' because in build-max-heap algo, we need the array length
        build_max_heap(arr, heap_end_pos + 1)

         
heapSort(arr)
print(arr)

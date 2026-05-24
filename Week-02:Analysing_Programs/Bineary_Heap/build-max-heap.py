#PCDIT

# PROBlEM
# Input: any list[int]
# Output: none
# Process: reorder to achieve max-heap for the whole binary tree.
# not just half of the nodes (like in max-heapify)
# no assumption here~

# TEST CASES (in the doc )
# basic idea: it is proven that elements from index (n/2) to (n - 1) are
# all leaves(node with no childs)
# we just need to apply max-heapify with elements from (n/2 - 1) move up to
# position 0, in that way, we will achieve the max-heap property satisfaction


# DESIGN OF ALGO:
# def heapify(A):
# version: 1
# Input:
#   - A = array storing the heap
# Output: None, restore the element in place
# Steps:
# 1. n = array length
# 2. starting_index = integer_division(n / 2) - 1
# 3. for current_index from starting_index down to 0 (moving backwards), do:
#     3.1 call max-heapify(array, current_index)

# IMPLEMENTATION
array = [1, 2, 8, 7, 14, 9, 3, 10, 4, 16] #represented as a heap (complete binary tree)
print(array)

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

def max_heapify(arr, indexOfCurrentNode):
    current_i = indexOfCurrentNode #start from index of current node (input)
    
    while( left(current_i) < len(arr) ): #ensure that the current node have children
        left_i = left(current_i)
        right_i = right(current_i)
        
        # In case where it only has one child (left) then the largest child element is the left
        if( right(current_i) >= len(arr) ):
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
            
        # move to the position (index Bof the larger child node) to continue analyzing
        current_i = max_child_i
        
def build_max_heap(arr):
    n = len(arr)
    starting_index = (n // 2) - 1
    
    for current_index in range(starting_index, -1, -1):
        max_heapify(arr, current_index)

build_max_heap(array)
print(array)

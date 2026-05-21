# PCDIT

# PROBLEM STATEMENT:
# Input: index of current node in a heap
# Output: none
# Process: re-order elements in a heap to make max-heap property satisfied
# from the current index node
# Asssumption:
# left/right child forms a tree that satisfies max-heap property
# only the current node with its children may not satisfy max-heap property


# TEST CASES (inside the doc): all child forms a max-heap prop satisfied tree
# basic idea: see the 2 childs of the current node
# compare the element of current node w elements of the 2 childs
# -> swap with the larger element

# after we swap, we need to verify if the tree that forms by the child satisfies
# the max-heap. If not, need to repeat the process of swapping but apply on the 
# just swapped child node element


# DESIGN OF ALGORITHM

# pseudocode
# def max-heapify(A, i):
# version: 1
# Input:
#   - A = array storing the heap
#   - i = index of the current node to restore max-heap property
# Output: None, restore the element in place
# Steps:
# 1. current_i = i # current index starting from input i
# 2. As long as ( left(current_i) < length of array), do:
#     2.1 max_child_i = get the index of largest child of the node current_i
#     2.2 if array[max_child_i] > array[current_i], do:
#         2.2.1 swap( array[max_child_i], array[current_i])
#     2.3 current_i = max_child_i # move to the index of the largest child

# IMPLEMENTATION
arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1] #represented as a heap (complete binary tree)
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

def max_heapify(arr, indexOfCurrentNode):
    current_i = indexOfCurrentNode #start from index of current node (input)
    while( left(current_i) < len(arr) ): #ensure that the current node have children
        left_i = left(current_i)
        right_i = right(current_i)
        
        if ( right_i >= len(arr) ): #if a node has only 1 child then max child = that one
            max_child_i = left_i
        else:
            max_child = max( arr[left_i], arr[right_i] )
            
            # Finding the index of the larget child node element
            if( max_child == arr[left(current_i)] ):
                max_child_i = left(current_i)
            else:
                max_child_i = right(current_i)
        
        # if the child node element larger than current node element, swap (push the node element down)
        if arr[max_child_i] > arr[current_i]:
            arr[max_child_i], arr[current_i] = arr[current_i], arr[max_child_i]
            
        # move to the position (index of the larger child node) to continue analyzing
        current_i = max_child_i
        
    return arr
    
max_heapify(arr, 1)
print(arr)


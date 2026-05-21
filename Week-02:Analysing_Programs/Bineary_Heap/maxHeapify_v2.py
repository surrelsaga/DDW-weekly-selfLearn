# PCDIT: (same as v1)

# Optimization: When we iterate until some points
# where we don't need to swap anymore
# that is where we can stop, no need to continue going down the tree (heap)
# anymore. 100% that it alr satisfied the max-heap property

# DESIGN OF ALGO:
# def max-heapify(A, i):
# version: 1
# Input:
#   - A = array storing the heap
#   - i = index of the current node to restore max-heap property
# Output: None, restore the element in place
# Steps:
# 1. current_i = i # current index starting from input i
# 2. swapped = True
# 3. As long as ( left(current_i) < length of array and swapped = True), do:
    # 3.1 swapped = False
#     3.2 max_child_i = get the index of largest child of the node current_i
#     3.3 if array[max_child_i] > array[current_i], do:
#         3.3.1 swap( array[max_child_i], array[current_i])
#         3.3.2 swapped = True
#     3.4 current_i = max_child_i # move to the index of the largest child


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
        else: #if no swap then, it satisfies the property alr -> stop the loop
            break
            
        # move to the position (index of the larger child node) to continue analyzing
        current_i = max_child_i
    
max_heapify(arr, 1)
print(arr)

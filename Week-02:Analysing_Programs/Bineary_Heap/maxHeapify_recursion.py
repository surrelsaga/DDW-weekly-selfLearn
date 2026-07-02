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
    # Base case: no children
    if left(indexOfCurrentNode) >= len(arr):
        return arr
    
    # Recursive case
    left_i = left(indexOfCurrentNode)
    right_i = right(indexOfCurrentNode)
    
    if right_i >= len(arr):
        max_child_i = left_i
    else:
        if arr[left_i] >= arr[right_i]:
            max_child_i = left_i
        elif arr[left_i] < arr[right_i]:
            max_child_i = right_i
    
    if arr[max_child_i] > arr[indexOfCurrentNode]:
        arr[max_child_i], arr[indexOfCurrentNode] = arr[indexOfCurrentNode], arr[max_child_i]
    else:
        return arr
        
    return max_heapify(arr, max_child_i)
    
arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1] #represented as a heap (complete binary tree)
print(arr)

max_heapify(arr, 1)
print(arr)

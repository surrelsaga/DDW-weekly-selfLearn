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

# Modified max_heapify, the end of array is now changing
def max_heapify(arr, indexOfCurrentNode, n=None):
    if n is None:
        n = len(arr)

    # Base case: no children
    if left(indexOfCurrentNode) >= n:
        return arr
    
    # Recursive case
    left_i = left(indexOfCurrentNode)
    right_i = right(indexOfCurrentNode)
    
    if right_i >= n:
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
        
    return max_heapify(arr, max_child_i, n)

def build_max_heap(arr):
    n = len(arr)
    starting_index = (n // 2) - 1
    
    for current_index in range(starting_index, -1, -1):
        max_heapify(arr, current_index)

def heap_sort(arr, head_end_pos=None):
    if head_end_pos is None:
        build_max_heap(arr)
        head_end_pos = len(arr) - 1
    
    # Base case: we keep repeating building max heap until reaching the 2nd element from the last element
    # that's when we know all the elements are in correct position (array sorted)
    if head_end_pos <= 0:
        return
    
    # After build_max_heap for the first time, confirm the largest is in root node
    # Swap with the last element, and next time max-heapify (from root node) to the end (except the swapped element)
    arr[0], arr[head_end_pos] = arr[head_end_pos], arr[0]
    
    # build-max-heap again from 0 to n - 1
    max_heapify(arr, 0, head_end_pos)
    
    # then keep recursing and swapping
    heap_sort(arr, head_end_pos - 1)
    
    
arr = [1, 2, 8, 7, 14, 9, 3, 10, 4, 16]
print(arr)
heap_sort(arr)
print(arr)

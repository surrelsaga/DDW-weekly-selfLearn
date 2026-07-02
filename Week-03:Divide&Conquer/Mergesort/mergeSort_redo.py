def merge_sort(arr):
    # This is the base case, we split the array until all the subarrays length is exactly 1
    if len(arr) <= 1:
        return
    
    # Recursive case: after done splitting
    # mergesort 2 subarrays at once, working backward
    # after sort, merge 2 subarrays to form a bigger one
    # we have pairs of many bigger subarrays
    # repeat: mergesort subarrays -> merge
    
    # Split the array in halves (subarrays)
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]
    
    # recursively merge sort these subarrays
    merge_sort(left_arr)
    merge_sort(right_arr)
    
    # Merge()
    # merge these subarrays together to create sorted big arrays.
    # at this points, 2 subarrays are already sorted
    
    # pointers
    i = 0 # keep track of left array index
    j = 0 # keep track of right array index
    k = 0 # merged array index
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            # if found which one is smaller, put in the merged array
            arr[k] = left_arr[i]
            i += 1 # move pointer to the right by 1 (left array)
            k += 1 # move pointer to the right by 1 (merged array)
        else:
            arr[k] = right_arr[j]
            j += 1 # move pointer to the right by 1 (right array)
            k += 1 # move pointer to the right by 1 (merged array)
            
    # In case of there is no element left in either of 2 subarrays
    # Just put those remaining elements in the merged array
    
    # no elements left in right array
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
        
    # no elements left in left array
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
            
arr = [6, 7, 9, 10, 4, 7, 3, 6, 9, 12]

merge_sort(arr)

print(arr)

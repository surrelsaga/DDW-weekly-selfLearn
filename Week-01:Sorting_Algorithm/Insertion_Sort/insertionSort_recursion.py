# Recurion of the v2

def insertion_sort(arr, n=None):
    if n is None:
        n = len(arr)
    
    if n <= 1:
        return arr
    
    # Recursively sort: we start from the rightmost, go backwards until we reach second element
    # Then start the algorithm from the second element
    insertion_sort(arr, n-1)
    
    # Insert the arr[i] into its correct position
    innerindex = n - 1
    numberToTakeOut = arr[n - 1]
    while innerindex > 0 and arr[innerindex - 1] > numberToTakeOut:
        arr[innerindex] = arr[innerindex - 1]
        innerindex -= 1
    
    arr[innerindex] = numberToTakeOut
    
    return arr
        
data = [16, 14, 10, 8, 7, 8, 3, 2, 4, 1]
print(insertion_sort(data))
    
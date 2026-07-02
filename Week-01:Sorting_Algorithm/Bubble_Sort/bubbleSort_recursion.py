# Recursion of v3 (inner loop is decremented by 1)
def bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)
    
    if n <= 1:
        return arr
    
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
    
    return bubble_sort(arr, n - 1)

data = [16, 14, 10, 8, 7, 8, 3, 2, 4, 1]
print(bubble_sort(data))

def is_min_heap(arr):
    n = len(arr)
    
    for i in range(n):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        
        if left_child < n and arr[i] > arr[left_child]:
            return False
        
        if right_child < n and arr[i] > arr[right_child]:
            return False
    
    return True

# Example usage
arr = [3, 8, 10, 17, 19, 26, 22, 31, 42, 50]
print(is_min_heap(arr))  # Output: True

arr = [9, 14, 18, 23, 50, 26, 32, 27, 36, 35]
print(is_min_heap(arr))  # Output: False

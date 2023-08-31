def min_heap_to_max_heap(arr):
    n = len(arr)
    
    # Build a max heap using the elements from the min heap
    for i in range(n):
        j = i
        
        # Fix the max heap property for the current element
        while j > 0:
            parent = (j - 1) // 2
            if arr[j] > arr[parent]:
                arr[j], arr[parent] = arr[parent], arr[j]
                j = parent
            else:
                break

# Example usage
min_heap = [1,2,3,4,5,6]
print("Min Heap:", min_heap)

min_heap_to_max_heap(min_heap)
print("Max Heap:", min_heap)

def merge_k_sorted_lists(lists):
    combined = []
    for lst in lists:
        combined.extend(lst)
    
    combined.sort()
    return combined

# Example usage
k_sorted_lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]
result = merge_k_sorted_lists(k_sorted_lists)
print(result)  # Output: [1, 1, 2, 3, 4, 4, 5, 6]

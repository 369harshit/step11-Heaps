import heapq

def min_cost_to_connect_ropes(ropes):
    heapq.heapify(ropes)  # Convert the input list into a min-heap

    total_cost = 0
    while len(ropes) > 1:
        # Extract the two smallest ropes from the heap
        min1 = heapq.heappop(ropes)
        min2 = heapq.heappop(ropes)

        # Connect the two ropes and add the cost to the total
        cost = min1 + min2
        total_cost += cost

        # Insert the connected rope back into the heap
        heapq.heappush(ropes, cost)

    return total_cost

# Example usage
ropes = [4,3,2,6]
result = min_cost_to_connect_ropes(ropes)
print("Minimum cost to connect ropes:", result)  # Output will vary based on input

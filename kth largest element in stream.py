import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Example usage
commands = ["KthLargest", "add", "add", "add", "add", "add"]
arguments = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

result = []
kth_largest = None

for i in range(len(commands)):
    command = commands[i]
    argument = arguments[i]

    if command == "KthLargest":
        kth_largest = KthLargest(*argument)
        result.append(None)
    elif command == "add":
        result.append(kth_largest.add(*argument))

print(result)  # Output should be [None, 4, 5, 5, 8, 8]

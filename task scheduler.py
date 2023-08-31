def least_interval(tasks, n):
    task_counts = [0] * 26  # There are 26 possible letters (A to Z)
    
    for task in tasks:
        task_counts[ord(task) - ord('A')] += 1
    
    task_counts.sort(reverse=True)  # Sort task counts in descending order
    
    max_count = task_counts[0]
    idle_time = (max_count - 1) * n
    
    for count in task_counts[1:]:
        idle_time -= min(max_count - 1, count)
    
    idle_time = max(0, idle_time)  # Idle time cannot be negative
    total_time = len(tasks) + idle_time
    
    return total_time

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
output = least_interval(tasks, n)
print(output)  # Output should be 8

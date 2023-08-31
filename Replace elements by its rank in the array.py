n = 6
arr = [20, 15, 26, 2, 98, 6]
for i in range(n):
    s = set()
    for j in range(n):
        if arr[j] < arr[i]:
            s.add(arr[j])
    print(len(s) + 1, end=" ")

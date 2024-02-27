import sys
input = sys.stdin.readline

arr = [0 for _ in range(13)]
arr_node = [[] for _ in range(13)]
for _ in range(12):
    x, y = map(int, input().rstrip().split())
    arr[x] += 1
    arr[y] += 1
    arr_node[x].append(y)
    arr_node[y].append(x)
for i in range(1, 13):
    if arr[i] == 3:
        now = []
        for a in arr_node[i]: now.append(arr[a])
        now.sort()
        if now == [1, 2, 3]:
            print(i)
            break
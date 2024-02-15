import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
    arr.sort(key=lambda x:x[0])

    result = n
    min_value = arr[0][1]
    for i in range(1, n): 
        if arr[i][1] > min_value: result -= 1
        min_value = min(min_value, arr[i][1])
    print(result)
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
    result = 0
    for i in range(n):
        if max(arr[i]) >= 0: result += max(arr[i])
    
    print(result)
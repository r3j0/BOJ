import sys
input = sys.stdin.readline
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = []
    for _ in range(n):
        a, b = input().split()
        arr.append([int(a), b])
    
    arr.sort(key=lambda x:-x[0])

    print(arr[0][1])
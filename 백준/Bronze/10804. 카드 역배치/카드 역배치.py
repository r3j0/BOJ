import sys
input = sys.stdin.readline

arr = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().rstrip().split())
    go = arr[a-1:b][::-1]
    for i in range(a-1, b):
        arr[i] = go[i-a+1]

print(' '.join(map(str, arr)))
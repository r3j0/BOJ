import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
able = []
for i in range(n - 1):
    for j in range(i + 1, n):
        able.append([arr[i], arr[j]])

for _ in range(k-1):
    arr = list(map(int, input().rstrip().split()))
    gone = []
    for a1, a2 in able:
        if arr.index(a1) <= arr.index(a2): gone.append([a1, a2])
    
    able = gone

print(len(able))
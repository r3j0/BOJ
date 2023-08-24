import sys
input = sys.stdin.readline

n, d = map(int, input().rstrip().split())
arr = [0 for _ in range(10)]
for i in range(1, n+1): 
    arr[d] += str(i).count(str(d))

print(arr[d])
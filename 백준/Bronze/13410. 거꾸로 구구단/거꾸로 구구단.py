import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = []
for i in range(1, k+1):
    arr.append(str(n*i)[::-1])
arr = list(map(int, arr))
print(max(arr))

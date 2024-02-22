import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for i in range(n):
    order = list(map(int, input().rstrip().split()))[1:]
    arr.append(sum(order))
arr.sort()
for i in range(1, n):
    arr[i] += arr[i-1]

print(sum(arr))
import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
c, d = map(int, input().rstrip().split())

arr = [0 for _ in range(101)]
for i in range(a, b): arr[i] = 1
for i in range(c, d): arr[i] = 1

print(sum(arr))
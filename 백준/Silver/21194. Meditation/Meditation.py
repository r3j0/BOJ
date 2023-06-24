import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = []
for _ in range(n): arr.append(int(input().rstrip()))
arr.sort(reverse=True)
sum = 0
for i in range(k): sum += arr[i]
print(sum)
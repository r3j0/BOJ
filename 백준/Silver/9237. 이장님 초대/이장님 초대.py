import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort(reverse=True)

max_days = 1
for i in range(n):
    max_days = max(max_days, (i+1)+arr[i])

print(max_days + 1)
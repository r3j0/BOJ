import sys
input = sys.stdin.readline

left, right, k = map(int, input().rstrip().split())
for _ in range(k):
    if left <= right: left += 1
    else: right += 1

print(min(left, right) * 2)
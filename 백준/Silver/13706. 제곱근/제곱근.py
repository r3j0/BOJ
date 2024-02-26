import sys
input = sys.stdin.readline

n = int(input().rstrip())
start = 1
end = n
while start < end:
    mid = (start + end) // 2
    if mid*mid < n:
        start = mid + 1
    elif mid*mid > n:
        end = mid - 1
    else:
        start = mid
        break

print(start)
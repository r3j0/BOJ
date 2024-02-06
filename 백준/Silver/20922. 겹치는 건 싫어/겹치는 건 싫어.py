# 너 투 포인터지?
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

start = 0
end = 1
now = {i:0 for i in range(1, 100001)}

now[arr[0]] = 1
result = 0
while n >= end:
    result = max(result, end - start)
    if n == end: break
    if n > end and now[arr[end]] < k:
        now[arr[end]] += 1
        end += 1
    else:
        while now[arr[end]] >= k and start < end - 1:
            now[arr[start]] -= 1
            start += 1
        if start == end - 1:
            now[arr[start]] -= 1
            start += 1
            now[arr[end]] += 1
            end += 1

print(result)
# 1806 : 부분합
import sys
input = sys.stdin.readline

n, s = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
left = 0
right = 0
sums = arr[0]
ans = n+1

while right < n:
    if sums >= s:
        ans = min(ans, right - left + 1)
        if left == right:
            right += 1
            if right < n:
                sums += arr[right]
        sums -= arr[left]
        left += 1
    else:
        right += 1
        if right < n:
            sums += arr[right]

if ans == n + 1: ans = 0
print(ans)
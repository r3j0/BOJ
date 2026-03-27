# 32630 
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort()
ans = sum(arr)
ans = max(ans, sum(arr[2:]) + (arr[0] * arr[1] * 2))
ans = max(ans, sum(arr[:n-2]) + (arr[n-1] * arr[n-2] * 2))
print(ans)

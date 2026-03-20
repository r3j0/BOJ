# 10986 : 나머지 합
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

# 누적 합 : arr[i] % m 이 등장한 횟수
arr = list(map(int, input().rstrip().split()))

sums = [0 for _ in range(m)]
sums[0] = 1
now = 0
ans = 0
for i in range(n):
    now = (now + arr[i]) % m

    ans += sums[now]
    sums[now] += 1

print(ans)
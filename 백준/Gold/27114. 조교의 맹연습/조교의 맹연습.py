import sys
input = sys.stdin.readline

a, b, c, k = map(int, input().rstrip().split())

dp = [float('inf') for _ in range(k+1)] 
dp[0] = 0

# 1. 좌로 돌아 - 좌로 돌아 - 뒤로 돌아
# 2. 우로 돌아 - 우로 돌아 - 뒤로 돌아
# 3. 좌로 돌아 - 우로 돌아
# 4. 뒤로 돌아 - 뒤로 돌아
# 5. 좌로 돌아 - 좌로 돌아 - 좌로 돌아 - 좌로 돌아
# 6. 우로 돌아 - 우로 돌아 - 우로 돌아 - 우로 돌아
arr = [a+a+c, b+b+c, a+b, c+c, a+a+a+a, b+b+b+b]

for energy in range(1, k+1):
    for thing in range(6):
        if energy >= arr[thing]:
            dp[energy] = min(dp[energy], dp[energy - arr[thing]] + (3 if thing <= 1 else (2 if thing <= 3 else 4)))

print(dp[k] if dp[k] != float('inf') else -1)
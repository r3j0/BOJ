import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(input().rstrip()) for _ in range(n)]

sum_arr = sum(arr)

# dp[i][j] = i 몸무게를 만들 수 있음 j 개의 사람으로
dp = [[0 for _ in range(n+1)] for _ in range(sum_arr+1)]

for ai in range(n):
    for weight in range(sum_arr, -1, -1):
        for k in range(n):
            if weight == 0:
                dp[arr[ai]][1] = 1
            elif dp[weight][k] == 1 and weight + arr[ai] <= sum_arr:
                dp[weight + arr[ai]][k + 1] = 1

    #for weight in range(sum_arr + 1):
    #    for k in range(1, n):
    #        if dp[weight][k] == 1:
    #            dp[abs(weight - arr[ai])][k + 1] = 1
max_diff = -1
max_our = 0
if n % 2 == 1:    
    # 홀수 팀 판정
    for i in range(1, sum_arr+1):
        our = n // 2
        enemy = n - (n // 2)

        if dp[i][our] == 1 and dp[sum_arr - i][enemy] == 1:
            if max_diff == -1 or max_diff > abs(i - (sum_arr - i)):
                max_diff = abs(i - (sum_arr - i))
                max_our = i
else:
    # 짝수 팀 판정
    for i in range(1, sum_arr+1):
        our = n // 2

        if dp[i][our] == 1 and dp[sum_arr - i][our] == 1:
            if max_diff == -1 or max_diff > abs(i - (sum_arr - i)):
                max_diff = abs(i - (sum_arr - i))
                max_our = i
print(min(max_our, sum_arr - max_our), max(max_our, sum_arr - max_our))
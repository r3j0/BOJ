import sys
input = sys.stdin.readline

lighter = input().rstrip()
smallant = input().rstrip()

MOD = 1000000007

def rps(l, s):
    if l == 'R':
        if s == 'R': return 0
        elif s == 'P': return 2
        else: return 1
    elif l == 'P':
        if s == 'R': return 1
        elif s == 'P': return 0
        else: return 2
    else:
        if s == 'R': return 2
        elif s == 'P': return 1
        else: return 0
def rps_digit(c):
    if c == 'R': return 0
    elif c == 'P': return 1
    else: return 2

# dp[i] i번째 정보까지의 경우의 수
# R 무승부 R lighter R smallant
# P 무승부 P lighter P smallant
# S 무승부 S lighter S smallant
dp = [[0, 0, 0] for _ in range(3)]
for i in range(1, len(smallant)+1):
    new_dp = [[dp[a][b] for b in range(3)] for a in range(3)]
    new_dp[rps_digit(smallant[i-1])][rps(lighter, smallant[i-1])] += 1
    
    if smallant[i-1] == 'R':
        new_dp[0][0] += dp[0][0] + dp[0][2]
        new_dp[0][1] += sum(dp[1])
        new_dp[0][2] += sum(dp[2])
    elif smallant[i-1] == 'P':
        new_dp[1][0] += dp[1][0] + dp[1][2]
        new_dp[1][1] += sum(dp[2])
        new_dp[1][2] += sum(dp[0])
    else:
        new_dp[2][0] += dp[2][0] + dp[2][2]
        new_dp[2][1] += sum(dp[0])
        new_dp[2][2] += sum(dp[1])
    
    for a in range(3):
        for b in range(3):
            dp[a][b] = new_dp[a][b] % MOD

res = 0
for a in range(3):
    for b in range(3):
        res += dp[a][b]

print(res % MOD)
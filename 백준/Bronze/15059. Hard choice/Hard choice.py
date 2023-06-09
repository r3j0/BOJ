import sys
input = sys.stdin.readline

able = list(map(int, input().rstrip().split()))
choi = list(map(int, input().rstrip().split()))
result = 0
for i in range(3):
    if choi[i] - able[i] > 0: result += choi[i] - able[i]

print(result)
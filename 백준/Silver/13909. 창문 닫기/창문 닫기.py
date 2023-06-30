# 약수의 개수가 홀수면 열리고,
# 약수의 개수가 짝수면 닫힌다

# 1 + 합성수이면서 약수의 개수가 홀수인 수 ( 4, 홀수려면 제곱수여야함 9 


import sys
input = sys.stdin.readline

n = int(input().rstrip())

cnt = 1
now = 2
while now**2 <= n:
    cnt += 1
    now += 1

print(cnt)
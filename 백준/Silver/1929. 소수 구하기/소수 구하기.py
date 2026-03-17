# 1929 : 소수 구하기
import sys 
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())

prime = [False for _ in range(n+1)]
prime[0] = True
prime[1] = True
for i in range(2, n+1):
    j = 2
    while i * j <= n:
        prime[i * j] = True
        j += 1

for i in range(m, n+1):
    if not prime[i]:
        print(i)
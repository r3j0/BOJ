# 2247 : 실질적 약수
import sys
input = sys.stdin.readline

# 1부터 n까지 모든 약수의 합 - (n * (n+1) // 2 + n)

"""
16 
1 2 4 8 16
15
1 3 5 15
14
1 2 7 14
13
1 13
12
1 2 3 4 6 12
"""

# i 의 약수 d 를 세는 것이 아닌, d의 배수가 1~n 안에 몇개 들었는지를 보는게 더 쉽다.
# harmonic-lemma
n = int(input().rstrip())
MOD = 1_000_000
ans = 0

i = 2
j = 0
while i <= n:
    # i ~ j 까지의 수가 n // i 번 등장합니다.
    j = n // (n // i)
    ans = (ans + (((j*(j+1)//2) - (i*(i-1)//2)) * (n//i-1))) % MOD
    i = j + 1

print(ans)
# 1457 : 정확해
import sys
input = sys.stdin.readline

a, b, n = map(int, input().rstrip().split())

# 목표 : A ~ A+B 까지 멋진 약수 개수
# = A ~ A+B 까지 약수 개수 - A ~ A+B 까지 멋지지 않은 약수 개수 (즉, M % K^N == 0)

# 1. A ~ A+B 까지 약수 개수 : harmonic-lemma
# 2. A ~ A+B 까지 멋지지 않은 약수 개수 : i^N 이므로 수가 급격히 증가. 직접 탐색

# 1.
res1 = 0

i = 1
j = 0
while i <= a + b:
    j = (a + b) // ((a + b) // i)
    res1 += (a + b) // i * (j - i + 1)
    i = j + 1

i = 1
j = 0
while i <= a - 1:
    j = (a - 1) // ((a - 1) // i)
    res1 -= (a - 1) // i * (j - i + 1)
    i = j + 1

res1 -= b + 1 # +) K가 M보다 작다는 조건. A ~ A+B 까지 자기 자신 약수를 지워야 한다.
if a == 1:    # +) 2번을 구하면 1이 구간 길이만큼 지워지게 되는데, 
    res1 += 1 #    A가 1이라면 res1 -= b + 1에서 1이 같이 지워진다. 또 지워지는거 방지

# 2.
res2 = 0
i = 1
while i ** n <= a + b:
    res2 += (a + b) // (i ** n)
    i += 1

i = 1
while i ** n <= a - 1:
    res2 -= (a - 1) // (i ** n)
    i += 1

print(res1 - res2)
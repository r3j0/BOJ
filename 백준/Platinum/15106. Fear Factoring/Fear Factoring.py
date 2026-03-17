# 15106 : Fear Factoring
import sys
input = sys.stdin.readline

# B 까지 모든 약수의 합 - (A - 1) 까지 모든 약수의 합
a, b = map(int, input().rstrip().split())

def lemma(n):
    res = 0
    i = 1
    j = 0
    while i <= n:
        j = n // (n // i)
        res += n // i * ((j * (j + 1) // 2) - (i * (i - 1) // 2))
        i = j + 1
    return res

print(lemma(b) - lemma(a-1))
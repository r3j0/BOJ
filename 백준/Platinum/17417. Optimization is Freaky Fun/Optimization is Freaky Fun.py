# 17417 : Optimization is Freaky Fun
import sys
input = sys.stdin.readline

def lemma(n, k):
    res = 0
    i = 1
    j = 0
    while i <= k:
        j = min(k, n // (n // i))
        res += (n // i) * (j - i + 1)
        i = j + 1
    return res

def solve(n, s, e):
    return lemma(n, e) - lemma(n, s - 1)

q = int(input().rstrip())
for _ in range(q):
    n, s, e = map(int, input().rstrip().split())
    print(solve(n, s, e))
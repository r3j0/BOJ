import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())
hando = 60 + k if 60 + k <= n else n
remain = n - hando if n - hando > 0 else 0
print(hando * 1500 + remain * 3000)
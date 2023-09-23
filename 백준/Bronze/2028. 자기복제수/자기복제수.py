import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    if str(n**2)[-len(str(n)):] == str(n): print('YES')
    else: print('NO')
import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

ns = s * len(t)
nt = t * len(s)

print(1 if ns == nt else 0)
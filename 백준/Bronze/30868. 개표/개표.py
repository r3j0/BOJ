import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    print(('++++ '*(n//5)) + ('|'*(n%5)))
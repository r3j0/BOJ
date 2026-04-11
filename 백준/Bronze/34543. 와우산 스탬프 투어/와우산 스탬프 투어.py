import sys
input = sys.stdin.readline

n = int(input().rstrip())
w = int(input().rstrip())
print(max(0, n*10 + (20 if n>=3 else 0) + (50 if n==5 else 0) - (15 if w > 1000 else 0)))
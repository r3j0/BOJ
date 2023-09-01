import sys
input = sys.stdin.readline

h, m = map(int, input().rstrip().split())

result = h * 60 + m - 45 + (1440 if h * 60 + m - 45 < 0 else 0)
print(result // 60, result % 60)
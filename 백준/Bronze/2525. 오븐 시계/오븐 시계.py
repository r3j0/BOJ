import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
c = int(input().rstrip())

result = a * 60 + b + c - (1440 if a * 60 + b + c >= 1440 else 0)
print(result // 60, result % 60)
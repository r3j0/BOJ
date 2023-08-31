import sys
input = sys.stdin.readline

year = int(input().rstrip())
print(1 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 0)
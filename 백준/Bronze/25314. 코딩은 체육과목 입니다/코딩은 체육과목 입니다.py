import sys
input = sys.stdin.readline

n = int(input().rstrip())
print(('long '*(n//4)) + 'int')
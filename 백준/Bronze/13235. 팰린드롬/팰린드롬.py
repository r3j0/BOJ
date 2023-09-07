import sys
input = sys.stdin.readline

s = input().rstrip()
if s == s[::-1]: print('true')
else: print('false')
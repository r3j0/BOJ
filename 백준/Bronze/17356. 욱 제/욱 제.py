import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
print(1/(1+(10**((b-a)/400))))
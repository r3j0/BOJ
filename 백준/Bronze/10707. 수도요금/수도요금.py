import sys
input = sys.stdin.readline

a = int(input().rstrip())
b = int(input().rstrip())
c = int(input().rstrip())
d = int(input().rstrip())
e = int(input().rstrip())

print(min(a * e, b if e <= c else b + (e-c)*d))
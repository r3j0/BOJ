import sys
input = sys.stdin.readline

a, b = input().rstrip().split()
print(max(int(a[::-1]), int(b[::-1])))
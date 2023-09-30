import sys
input = sys.stdin.readline

a, b, x, y = map(int, input().rstrip().split())
print(min([abs(a-b), abs(a-y)+abs(b-x), abs(a-x)+abs(b-y)]))
import sys
input = sys.stdin.readline

p, q = map(int, input().rstrip().split())
a, b = map(int, input().rstrip().split())

print(min(p, q) * a + max(q-p, 0) * b)
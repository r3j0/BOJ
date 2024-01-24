import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().rstrip().split())
one_line = w
two_line = min(w*2, s*2)
one_diag = min(w*2, s)

print(min(x, y) * (one_diag) + (abs(y - x) // 2 * two_line) + (abs(y - x) % 2 * one_line))
import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().rstrip().split())
print(((h//(1+n)) + (1 if h % (1+n) != 0 else 0)) * ((w//(1+m)) + (1 if w % (1+m) != 0 else 0)))
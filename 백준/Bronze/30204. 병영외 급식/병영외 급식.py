import sys
from collections import deque
input = sys.stdin.readline

n, x = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
print(1 if sum(arr) % x == 0 else 0)
import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
stack = deque()
result = [0 for _ in range(N)]

for i in range(N):
    while stack and stack[-1][0] > arr[i]:
        stack.pop()
    while stack and stack[0][1] <= i - L:
        stack.popleft()
    stack.append([arr[i], i])
    result[i] = stack[0][0]

sys.stdout.write(' '.join(map(str, result)))
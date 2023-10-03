import sys
import math
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    res = list(str(math.factorial(n)))
    while res[-1] == '0':
        del res[-1]
    print(res[-1])
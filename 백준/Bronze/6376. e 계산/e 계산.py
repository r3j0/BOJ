import sys
import math
input = sys.stdin.readline

def now(num):
    return 1 / math.factorial(num)

print('n e')
print('- -----------')

for n in range(10):
    result = 0
    for i in range(n+1):
        result += now(i)
    if n <= 1:
        print(n, int(result))
    elif n == 2:
        print(n, result)
    else:
        print(n, '%.9f'%result)
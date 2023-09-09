import sys 
import math
input = sys.stdin.readline

while True:
    b, n = map(int, input().rstrip().split())
    if b == n == 0: break

    max_diff = 1000010
    result = 0
    for i in range(1000010):
        if max_diff > abs(i**n - b):
            max_diff = abs(i**n - b)
            result = i
        if i**n > b: break
    
    print(result)
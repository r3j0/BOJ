import sys
import math
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

arr = [1 for _ in range(10000001)]
arr[0] = 0
arr[1] = 0
for i in range(2, int(math.sqrt(10000000))+1):
    if arr[i] == 0: continue
    for j in range(i**2, 10000001, i):
        arr[j] = 0

cnt = 0
for i in range(2, 10000001):
    now_a = a
    now_b = b
    if arr[i] == 1:
        while i <= now_b / i:
            if now_a / i <= i: cnt += 1
            now_a /= i
            now_b /= i
    
print(cnt)
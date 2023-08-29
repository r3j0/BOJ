# 10000
# 101 x 103
# 105 자리 까지 만들기

arr = [1 for _ in range(200)]
arr[0] = 0
arr[1] = 0

for i in range(2, 200):
    for j in range(2, 200):
        if i * j >= 200: continue
        arr[i * j] = 0

sosu = []
for i in range(200):
    if arr[i] == 1:
        sosu.append(i)

import sys
input = sys.stdin.readline

n = int(input().rstrip())
for i in range(len(sosu) - 1):
    if sosu[i] * sosu[i+1] > n:
        print(sosu[i] * sosu[i+1])
        break
import sys
input = sys.stdin.readline

p, k = map(int, input().rstrip().split())
arr = [0 for _ in range(k)]
i = 2
while i < k:
    j = 2
    while i * j < k:
        arr[i * j] = 1
        j += 1
    i += 1

done = 0
for i in range(2, k):
    if arr[i] == 1: continue
    if p % i == 0: 
        print('BAD', i)
        done = 1
        break

if done == 0: print('GOOD')
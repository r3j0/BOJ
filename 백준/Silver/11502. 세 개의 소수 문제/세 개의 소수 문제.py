arr = [0 for _ in range(1001)]
arr[0] = 1
arr[1] = 1
for i in range(2, 1001):
    j = 2
    while i*j <= 1000:
        arr[i*j] = 1
        j += 1

alls = []
for i in range(1001):
    if arr[i] == 0: alls.append(i)

import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    done = False
    for i in range(len(alls)-2):
        for j in range(i, len(alls)-1):
            for k in range(j, len(alls)):
                if alls[i] + alls[j] + alls[k] == n:
                    print(alls[i], alls[j], alls[k])
                    done = True
                    break
            if done == True: break
        if done == True: break
    
    if done == False: print(0)


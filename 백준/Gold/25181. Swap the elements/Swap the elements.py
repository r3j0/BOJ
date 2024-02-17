import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
narr = []
for a in arr: narr.append(a)

done = True
for i in range(n):
    if arr[i] == narr[i]:
        idx = i + 1
        while idx < n and narr[i] == narr[idx]: idx += 1
        if idx == n: 
            idx = i - 1
            while idx >= 0 and (narr[idx] == arr[i] or narr[i] == arr[idx]): idx -= 1
            if idx == -1:
                done = False
                break
        tmp = narr[i]
        narr[i] = narr[idx]
        narr[idx] = tmp
if done == True: print(' '.join(map(str, narr)))
else: print(-1)
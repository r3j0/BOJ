import sys
input = sys.stdin.readline

arr = []
for _ in range(9): arr.append(int(input().rstrip()))

on = []
for i in range(8):
    for j in range(i+1, 9):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            on = [i, j]
            break
    if len(on) != 0: break

del arr[j]
del arr[i]

arr.sort()
for a in arr: print(a)
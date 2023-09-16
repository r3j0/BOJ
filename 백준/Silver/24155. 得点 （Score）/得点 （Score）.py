import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for i in range(n):
    arr.append([int(input().rstrip()), i, 0])

arr.sort(key=lambda x:-x[0])

rank = 1
prank = 1
for i in range(n):
    if i == 0:
        arr[i][2] = rank
        prank += 1
    else:
        if arr[i-1][0] != arr[i][0]:
            rank = prank
        arr[i][2] = rank
        prank += 1

arr.sort(key=lambda x:x[1])
for i in range(n): print(arr[i][2])
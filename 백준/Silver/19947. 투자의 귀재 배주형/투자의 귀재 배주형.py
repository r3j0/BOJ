import sys
import math
input = sys.stdin.readline

h, y = map(int, input().rstrip().split())
arr = [[h, h, h] for _ in range(11)]
for i in range(1, y+1):
    #A
    arr[i][0] = math.floor(max(arr[i-1])*(105/100))
    #B
    if i >= 3:
        arr[i][1] = math.floor(max(arr[i-3])*(120/100))
    #C
    if i >= 5:
        arr[i][2] = math.floor(max(arr[i-5])*(135/100))

print(max(arr[y]))
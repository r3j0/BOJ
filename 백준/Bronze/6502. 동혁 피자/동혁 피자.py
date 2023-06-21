import math
import sys
input = sys.stdin.readline

t = 1
while True:
    arr = list(map(int, input().rstrip().split()))
    if len(arr) == 1: break

    res1 = arr[0]*2
    res2 = math.sqrt(arr[1]**2+arr[2]**2)
    if res1 >= res2:
        print("Pizza %d fits on the table."%t)
    else:
        print("Pizza %d does not fit on the table."%t)
    t += 1 
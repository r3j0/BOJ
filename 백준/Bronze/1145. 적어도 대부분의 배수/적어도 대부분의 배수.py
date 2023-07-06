import sys
from math import *
input = sys.stdin.readline

arr = list(map(int, input().rstrip().split()))

mins = 0
mins_avail = 0
for a1 in range(3):
    for a2 in range(a1+1, 4):
        for a3 in range(a2+1, 5):
            now = lcm(arr[a1], arr[a2], arr[a3])
            
            if mins_avail == 0 or mins > now:
                mins = now
                mins_avail = 1

print(mins)
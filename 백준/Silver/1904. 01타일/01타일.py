import sys
import math
input = sys.stdin.readline

first = 1
second = 2
n = int(input())

go = 3
if n == 1: print(first)
elif n == 2: print(second)
else:
    while True:
        now = (first+second) % 15746
        first = second
        second = now
        if go == n: break
        go += 1
    print(second) 

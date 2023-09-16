import sys
import math
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    corcnt = 0
    allcnt = 0
    while True:
        string = input().rstrip()
        if string == "":
            ratiof = corcnt / allcnt * 100
            print("Efficiency ratio is %g%%." %(round(100 - (allcnt-corcnt) / allcnt * 100, 1)))
            break
        for s in string:
            allcnt += 1
            if s != '#': corcnt += 1
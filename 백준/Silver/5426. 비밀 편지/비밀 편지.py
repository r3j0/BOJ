import sys
import math
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    string = input().rstrip()
    lens = int(math.sqrt(len(string)))
    arr = [['' for _ in range(lens)] for _ in range(lens)]

    for i in range(lens):
        for j in range(lens):
            arr[i][j] = string[i*lens+j]
    
    for j in range(lens - 1, -1, -1):
        for i in range(lens):
            print(arr[i][j], end='')
    print()
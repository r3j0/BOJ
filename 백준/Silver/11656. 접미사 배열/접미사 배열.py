import sys
input = sys.stdin.readline

string = input().rstrip()
arr = []
for i in range(len(string)):
    arr.append(string[i:])

arr.sort()
for a in arr: print(a)
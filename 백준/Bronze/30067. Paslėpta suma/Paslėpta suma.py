import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(10)]

for i in arr:
    if sum(arr) - i == i:
        print(i)
        break
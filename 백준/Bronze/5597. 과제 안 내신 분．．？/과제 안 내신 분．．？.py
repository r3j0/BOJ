import sys
input = sys.stdin.readline

arr = [0 for _ in range(31)]

for _ in range(28):
    num = int(input().rstrip())
    arr[num] = 1
        
for i in range(1, 31):
    if arr[i] == 0:
        print(i)
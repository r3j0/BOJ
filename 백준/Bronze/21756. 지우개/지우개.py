import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [i for i in range(1, n+1)]
while len(arr) != 1:
    new_arr = []
    for i in range(len(arr)):
        if i % 2 != 0:
            new_arr.append(arr[i])
    
    arr = new_arr

print(arr[0])
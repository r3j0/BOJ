import sys
input = sys.stdin.readline

string = input().rstrip()

arr = [1, 0, 0, 2]
for s in string:
    if s == 'A': arr[0], arr[1] = arr[1], arr[0]
    elif s == 'B': arr[0], arr[2] = arr[2], arr[0]
    elif s == 'C': arr[0], arr[3] = arr[3], arr[0]
    elif s == 'D': arr[1], arr[2] = arr[2], arr[1]
    elif s == 'E': arr[1], arr[3] = arr[3], arr[1]
    elif s == 'F': arr[2], arr[3] = arr[3], arr[2]

print(arr.index(1)+1)
print(arr.index(2)+1)
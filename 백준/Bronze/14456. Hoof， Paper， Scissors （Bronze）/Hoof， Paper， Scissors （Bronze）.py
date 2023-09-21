import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [0, 0]
for _ in range(n):
    string = input().rstrip()
    if string == '1 2' or string == '2 3' or string == '3 1': arr[0] += 1
    elif string == '1 3' or string == '3 2' or string == '2 1': arr[1] += 1
print(max(arr))
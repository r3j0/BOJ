import sys
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == 0: break
    arr = [input().rstrip() for _ in range(n)]
    new_arr = []
    for i in range(n):
        new_arr.append([arr[i].upper(), i])
    new_arr.sort(key=lambda x:x[0])
    print(arr[new_arr[0][1]])
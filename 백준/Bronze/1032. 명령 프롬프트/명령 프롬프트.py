import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n): arr.append(input().rstrip())

for i in range(len(arr[0])):
    now = {}
    for k in range(n):
        if not now.get(arr[k][i]): now[arr[k][i]] = 1
    
    if len(now) == 1:
        print(list(now.keys())[0], end='')
    else:
        print('?', end='')
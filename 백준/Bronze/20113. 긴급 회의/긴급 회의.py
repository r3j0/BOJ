import sys
input = sys.stdin.readline

n = int(input().rstrip())
tupyo = list(sorted(map(int, input().rstrip().split())))
arr = [(i, tupyo.count(i)) for i in range(n+1)]
arr.sort(key=lambda x:(-x[1], x[0]))
available = []

for i in range(len(arr)):
    if arr[0][1] == arr[i][1]:
        available.append(arr[i][0])

if len(available) == 1:
    if available[0] == 0: print('skipped')
    else: print(available[0])
elif len(available) == 2:
    if available[0] == 0: print(available[1])
    elif available[1] == 0: print(available[0])
    else: print('skipped')
else:
    print('skipped')
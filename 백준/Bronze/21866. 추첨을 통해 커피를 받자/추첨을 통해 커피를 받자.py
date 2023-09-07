import sys
input = sys.stdin.readline

arr = list(map(int, input().rstrip().split()))
score = [100, 100, 200, 200, 300, 300, 400, 400, 500]

done = 0
for i in range(len(arr)):
    if arr[i] > score[i]:
        done = 1
        break

if done == 1:
    print('hacker')
else:
    if sum(arr) >= 100: print('draw')
    else: print('none')
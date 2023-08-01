import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(int(input().rstrip()))

goal = sum(arr)
res = []
for i in range(8):
    for j in range(i+1, 9):
        if goal - arr[i] - arr[j] == 100:
            res = [i, j]
            break
    
    if len(res) > 0: break

for i in range(9):
    if i == res[0] or i == res[1]:
        continue
    print(arr[i])
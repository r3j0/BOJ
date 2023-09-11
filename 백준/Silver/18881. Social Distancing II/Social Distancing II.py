import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

arr.sort(key = lambda x:x[0])

min_distance = 1000001

for i in range(n - 1):
    if (arr[i][1] == 0 and arr[i+1][1] == 1) or (arr[i][1] == 1 and arr[i+1][1] == 0):
        min_distance = max(0, min(min_distance, arr[i+1][0] - arr[i][0] - 1))

cnt = 1
for i in range(n - 1):
    if arr[i][1] == 1 and arr[i+1][1] == 1 and arr[i+1][0] - arr[i][0] > min_distance:
        cnt += 1
    elif arr[i][1] == 0 and arr[i+1][1] == 1:
        cnt += 1

print(cnt)
    
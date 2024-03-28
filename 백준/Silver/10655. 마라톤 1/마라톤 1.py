import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

dist = [0 for _ in range(n-1)]
for i in range(n-1):
    dist[i] = abs(arr[i+1][0] - arr[i][0]) + abs(arr[i+1][1] - arr[i][1])

now_skip = abs(arr[2][0] - arr[0][0]) + abs(arr[2][1] - arr[0][1])
now_dist = (sum(dist) - dist[0] - dist[1])
res = now_dist + now_skip
#print(now_skip, now_dist)
#print(dist)
for i in range(3, n):
    now_skip = abs(arr[i][0] - arr[i-2][0]) + abs(arr[i][1] - arr[i-2][1])
    now_dist -= dist[i-1]
    now_dist += dist[i-3]
    #print(now_skip, now_dist)
    res = min(res, now_skip + now_dist)

print(res)
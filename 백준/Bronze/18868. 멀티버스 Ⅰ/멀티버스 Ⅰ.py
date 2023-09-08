import sys
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(m)]

done = 0
for a in range(m-1):
    for b in range(a+1, m):
        cnt = 0
        for i in range(n):
            for j in range(n):
                if arr[a][i] > arr[a][j] and arr[b][i] > arr[b][j]: cnt += 1
                elif arr[a][i] < arr[a][j] and arr[b][i] < arr[b][j]: cnt += 1
                elif arr[a][i] == arr[a][j] and arr[b][i] == arr[b][j]: cnt += 1
        
        if cnt == n*n: done += 1
print(done)
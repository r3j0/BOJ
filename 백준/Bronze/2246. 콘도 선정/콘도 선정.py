import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
result = 0
# 거리 / 숙박비
for i in range(n):
    done = 0
    for j in range(n):
        if i == j: continue
        if (arr[i][0] >= arr[j][0] and arr[i][1] >= arr[j][1]):
            done += 1
        
    if done == 0: 
        result += 1
print(result)
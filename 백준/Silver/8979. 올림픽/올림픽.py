import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
arr.sort(key=lambda x:(-x[1], -x[2], -x[3]))
grade = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        grade[arr[0][0]-1] = 1
    else:
        if arr[i-1][1:] == arr[i][1:]:
            grade[arr[i][0]-1] = grade[arr[i-1][0]-1]
        else:
            grade[arr[i][0]-1] = grade[arr[i-1][0]-1] + 1

print(grade[k-1])
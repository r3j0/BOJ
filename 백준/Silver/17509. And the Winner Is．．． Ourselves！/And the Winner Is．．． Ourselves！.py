import sys
input = sys.stdin.readline

arr = [list(map(int, input().rstrip().split())) for _ in range(11)]
arr.sort(key=lambda x:(x[0]))
now_time = 0
now_penalty = 0
for i in range(11):
    now_time += arr[i][0]
    now_penalty += arr[i][1] * 20 + now_time

print(now_penalty)
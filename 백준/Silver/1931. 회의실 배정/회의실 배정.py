import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    arr.append([a,b])

arr.sort(key=lambda x : (x[1], x[0]))

now = 0
time = 0
cnt = 0
while now < n:
    if time <= arr[now][0]:
        time = arr[now][1]
        cnt += 1

    now += 1

print(cnt)
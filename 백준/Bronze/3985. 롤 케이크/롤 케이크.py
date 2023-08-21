import sys 
input = sys.stdin.readline

l = int(input().rstrip())
arr = [0 for _ in range(l)]
n = int(input().rstrip())
max_predict = 0
max_number = 0
for i in range(n):
    a, b = map(int, input().rstrip().split())
    if max_predict < b - a + 1:
        max_predict = b - a + 1
        max_number = i + 1

    for k in range(a, b+1):
        if arr[k-1] == 0: arr[k-1] = i+1

rollcake = [[i+1, 0] for i in range(n)]
for i in range(l):
    if arr[i] != 0:
        rollcake[arr[i]-1][1] += 1

rollcake.sort(key=lambda x:-x[1])
print(max_number)
print(rollcake[0][0])
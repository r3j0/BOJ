import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

narr = []
for i in range(n):
    narr.append([arr[i], i, 0])

narr.sort(key=lambda x:(x[0], x[1]))
for i in range(n):
    narr[i][2] = i

narr.sort(key=lambda x:x[1])
for i in range(n):
    print(narr[i][2], end=' ')
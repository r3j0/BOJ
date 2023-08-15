import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
seat = [0 for _ in range(100)]
cnt = 0
for a in arr:
    if seat[a-1] == 0: seat[a-1] = 1
    else: cnt += 1

print(cnt)
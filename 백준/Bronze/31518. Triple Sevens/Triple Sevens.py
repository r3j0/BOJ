import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0
for _ in range(3):
    arr = list(map(int, input().rstrip().split()))
    if arr.count(7) > 0: cnt += 1

print(777 if cnt == 3 else 0)
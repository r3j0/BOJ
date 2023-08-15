import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
mode = 0
cnt = 0
for a in arr:
    if a == mode:
       cnt += 1
       mode = (mode + 1) % 3

print(cnt) 
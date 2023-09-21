import sys
input = sys.stdin.readline

money = {136:1000, 142:5000, 148:10000, 154:50000}

n = int(input().rstrip())
cnt = 0
for _ in range(n):
    width, _ = map(int, input().rstrip().split())
    cnt += money[width]

print(cnt)
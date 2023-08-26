import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0
for i in range(1, n+1):
    if i % sum(list(map(int, list(str(i))))) == 0:
        cnt += 1
print(cnt)
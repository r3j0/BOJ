import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0
for _ in range(n):
    string = input().rstrip()
    if string.find('01') != -1 or string.find('OI') != -1: cnt += 1
print(cnt)
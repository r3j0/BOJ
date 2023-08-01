import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()

idx = 0
cnt = 0
couple = 0
while idx < len(string):
    if string[idx] == 'L':
        couple = 1
        idx += 1
    cnt += 1
    idx += 1

print(cnt + couple)
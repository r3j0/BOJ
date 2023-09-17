import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()

cnt = 0
for i in range(n//2):
    if string[i] != string[n-1-i]: cnt += 1
print(cnt)
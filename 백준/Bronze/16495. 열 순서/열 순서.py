import sys 
input = sys.stdin.readline

string = input().rstrip()
cnt = 0
for s in string:
    cnt *= 26
    cnt += ord(s) - ord('A') + 1

print(cnt)
import sys
input = sys.stdin.readline

string = input().rstrip()
now = ""
cnt = 0
for s in string:
    if len(now) == 0:
        now += s
    else:
        if ord(now[-1]) >= ord(s):
            cnt += 1
            now = s
        else:
            now += s

if len(now) != "": cnt += 1
print(cnt)
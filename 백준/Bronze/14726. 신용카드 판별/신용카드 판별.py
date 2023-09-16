def check(s):
    arr = []
    for i in range(len(s)):
        if i % 2 == 0:
            now = int(s[i]) * 2
            while len(str(now)) != 1:
                now = sum(list(map(int, list(str(now)))))
            arr.append(now)
        else: arr.append(int(s[i]))
    if sum(arr) % 10 == 0: return 'T'
    else: return 'F'

import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    string = input().rstrip()
    print(check(string))
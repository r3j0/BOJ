import sys
input = sys.stdin.readline

string = input().rstrip()

dic = {}
for s in string:
    if dic.get(s): dic[s] += 1
    else: dic[s] = 1

if len(string) % 2 == 0:
    done = 0
    for dk in dic.keys():
        if dic[dk] % 2 == 1:
            done = 1
            break

    if done == 1: print("I'm Sorry Hansoo")
    else:
        now = dict(sorted(dic.items()))
        for dk in now.keys():
            for dn in range(now[dk]//2):
                print(dk, end='')
        for dk in reversed(now.keys()):
            for dn in range(now[dk]//2):
                print(dk, end='')
else:
    done = 0
    for dk in dic.keys():
        if dic[dk] % 2 == 1:
            done += 1

    if done != 1: print("I'm Sorry Hansoo")
    else:
        now = dict(sorted(dic.items()))
        for dk in now.keys():
            for dn in range(now[dk]//2):
                print(dk, end='')
        for dk in now.keys():
            if now[dk] % 2 == 1:
                print(dk, end='')
                break
        for dk in reversed(now.keys()):
            for dn in range(now[dk]//2):
                print(dk, end='')
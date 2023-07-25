import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()

lstack = 0
sstack = 0
result = 0
error = 0
for s in string:
    if error == 1: continue

    if s == 'L': lstack += 1
    elif s == 'S': sstack += 1
    elif s == 'R':
        if lstack > 0:
            lstack -= 1
            result += 1
        else:
            error = 1
    elif s == 'K':
        if sstack > 0:
            sstack -= 1
            result += 1
        else:
            error = 1
    else: result += 1

print(result)
import sys
input = sys.stdin.readline

string = list(input().rstrip())
arr = list(str(string).split('.'))

done = 0
for a in arr:
    if a == '': continue
    if len(a) % 2 == 1: 
        done = 1
        break

if done == 0:
    for s in range(len(string)):
        if string[s] == 'X':
            if string[s] == 'X' and s+3 <= len(string) - 1:
                xcnt = 0
                for i in range(s, s+4):
                    if string[i] == 'X':
                        xcnt += 1
                
                if xcnt == 4:
                    for i in range(s, s+4):
                        string[i] = 'A'

            if string[s] == 'X' and s+1 <= len(string) - 1:
                xcnt = 0
                for i in range(s, s+2):
                    if string[i] == 'X':
                        xcnt += 1
                
                if xcnt == 2:
                    for i in range(s, s+2):
                        string[i] = 'B'


if done == 1:
    print(-1)
else:
    print(''.join(string))
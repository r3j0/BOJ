import sys
input = sys.stdin.readline

string = input().rstrip()

joi = 0
ioi = 0
for i in range(len(string)):
    if string[i] == 'J':
        if (i+1 < len(string) and string[i+1] == 'O') and (i+2 < len(string) and string[i+2] == 'I'):
            joi += 1
    elif string[i] == 'I':
        if (i+1 < len(string) and string[i+1] == 'O') and (i+2 < len(string) and string[i+2] == 'I'):
            ioi += 1

print(joi)
print(ioi)
import sys
input = sys.stdin.readline

string = input().rstrip()
if string.count('_') > 0 and string[0] != '_' and string[-1] != '_' and string == string.lower(): # C++
    t = 0
    for i in range(len(string)-1):
        if string[i] == string[i+1] == '_': 
            t = 1
            print('Error!')
            break
    if t == 0:
        on = 0
        for i in range(len(string)):
            if string[i] == '_':
                on = 1
            else:
                if on == 1: print(chr(ord(string[i]) - 32), end='')
                else: print(string[i], end='')
                on = 0
elif string.count('_') == 0 and string[0] == string[0].lower() and string != string.lower():
    for i in range(len(string)):
        if 'A' <= string[i] <= 'Z':
            print('_', end='')
            print(chr(ord(string[i]) + 32), end='')
        else:
            print(string[i], end='')
elif string.count('_') == 0 and string == string.lower(): print(string)
else: print('Error!')
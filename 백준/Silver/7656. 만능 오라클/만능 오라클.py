import sys
input = sys.stdin.readline

string = input().rstrip()
start = 0
cnt = ""
for i in range(3, len(string)):
    if start == 0 and string[i-3:i+1] == 'What':
        start = 1
    elif start == 1:
        if string[i] == '?':
            print('Forty-two' + cnt + '.')
            cnt = ""
            start = 0
        elif string[i] == '.':
            cnt = ""
            start = 0
        else:
            cnt += string[i]
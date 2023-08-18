import sys
input = sys.stdin.readline

string = input().rstrip()
recording = 0
record_str = ""
for s in string:
    if recording == 0:
        if s == '(':
            recording = 1
        else:
            print(s, end='')
    else:
        if s == ')':
            recording = 0
            print(record_str[::-1], end='')
            record_str = ""
        else:
            record_str += s
import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()
if len(string) <= 25: print(string)
else:
    nstring = string[11:len(string)-11]
    if (nstring.count('.') == 1 and nstring[-1] == '.') or (nstring.count('.') == 0):
        print(string[:11] + "..." + string[len(string)-11:])
    else:
        print(string[:9] + "......" + string[len(string)-10:])
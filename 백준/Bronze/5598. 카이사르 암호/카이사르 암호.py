import sys
input = sys.stdin.readline

string = input().rstrip()
for s in string:
    print(chr(ord(s)-3 if ord(s)-3 >= ord('A') else ord(s)+23), end='')
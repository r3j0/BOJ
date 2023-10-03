import sys
input = sys.stdin.readline

string = input().rstrip()
arr = list(input().rstrip().split())
for i in string:
    if i in arr:
        print(chr(ord(i) + 32), end='')
    else:
        print(i, end='')
import sys
input = sys.stdin.readline

string = input().rstrip()
idx = 0
while idx < len(string):
    print(string[idx], end='')
    if string[idx] in ['a', 'e', 'i', 'o', 'u']:
        idx += 2
    idx += 1
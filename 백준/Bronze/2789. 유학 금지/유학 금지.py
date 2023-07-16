import sys
input = sys.stdin.readline

string = input().rstrip()
for s in string:
    if s not in ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']: print(s, end='')
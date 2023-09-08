import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()
idx = 0
while idx < len(string):
    print(string[idx], end='')
    idx += n
    
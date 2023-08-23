import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    string = input().rstrip()
    if string[len(string)//2-1] == string[len(string)//2]: print('Do-it')
    else: print('Do-it-Not')
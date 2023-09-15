import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range(n):
    string = input().rstrip()

    if string == 'P=NP': print('skipped')
    else: print(eval(string))
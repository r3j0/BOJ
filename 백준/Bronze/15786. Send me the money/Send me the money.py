import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
string = input().rstrip()
for _ in range(m):
    s = input().rstrip()
    idx = 0
    for i in s:
        if idx < len(string) and i == string[idx]:
            idx += 1
    
    if idx == len(string): print('true')
    else: print('false')
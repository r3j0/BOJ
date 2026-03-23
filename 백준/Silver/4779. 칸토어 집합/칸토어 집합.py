# 4779 : 칸토어 집합
import sys
input = sys.stdin.readline

def solve(n):
    if n == 0: 
        print('-', end='')
        return
    
    solve(n-1)
    print(' '*(3**(n - 1)),end='')
    solve(n-1)

try:
    while True:
        n = int(input().rstrip())
        solve(n)
        print()
except:
    pass
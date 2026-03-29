# 1914 : 하노이 탑
import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n = int(input().rstrip())

def solve(s, m, e, right):
    if right == 1:
        if n <= 20:
            print(s, e)
        return
    
    solve(s, e, m, right - 1)
    if n <= 20:
        print(s, e)
    solve(m, s, e, right - 1)

print((1 << n) - 1)
if n <= 20: solve(1, 2, 3, n)
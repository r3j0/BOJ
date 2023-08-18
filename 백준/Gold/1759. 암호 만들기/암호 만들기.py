import sys
input = sys.stdin.readline

l, c = map(int, input().rstrip().split())
arr = list(sorted(input().rstrip().split()))

def able(now_str):
    cnt = now_str.count('a') + now_str.count('e') + now_str.count('i') + now_str.count('o') + now_str.count('u')
    if cnt > 0 and len(now_str) - cnt > 1: return 1
    return 0

def backtracking(now_str, start):
    global l
    global c
    global arr

    if len(now_str) == l and able(now_str) == 1:
        print(now_str)
        return
    
    for i in range(start, c):
        backtracking(now_str + arr[i], i + 1)


backtracking("", 0)
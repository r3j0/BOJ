import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
for a in arr:
    now = a * 100 // n
    if 0 <= now <= 4: print(1, end=' ')
    elif 4 < now <= 11: print(2, end=' ')
    elif 11 < now <= 23: print(3, end=' ')
    elif 23 < now <= 40: print(4, end=' ')
    elif 40 < now <= 60: print(5, end=' ')
    elif 60 < now <= 77: print(6, end=' ')
    elif 77 < now <= 89: print(7, end=' ')
    elif 89 < now <= 96: print(8, end=' ')
    elif 96 < now <= 100: print(9, end=' ')
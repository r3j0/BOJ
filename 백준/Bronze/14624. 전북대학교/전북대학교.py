import sys
input = sys.stdin.readline

n = int(input().rstrip())
if n % 2 == 0: print('I LOVE CBNU')
else:
    print('*'*n)
    for i in range(n//2+1):
        print(' '*((n//2+1)-i-1), end='')
        print('*', end='')
        if i > 0:
            print(' '*(1+(i-1)*2), end='')
            print('*', end='')
        print()
import sys
input = sys.stdin.readline

digits = input().rstrip()

for i in range(4):
    for j in range(4):
        print('*' if ((int(digits[j])) & (1 << (3-i))) >> (3-i) else '.', end='')
        if j == 1: print('   ', end='')
        elif j != 3: print(' ', end='')
    print()

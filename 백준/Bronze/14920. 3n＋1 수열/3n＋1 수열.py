import sys
input = sys.stdin.readline

cn = int(input().rstrip())
n = 1

while cn != 1:
    if cn % 2 == 0: cn /= 2
    else: cn = 3*cn+1
    n += 1
print(n)
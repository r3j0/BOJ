import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()

ccnt = string.count('C')

if ccnt == n: print(n)
else: print(ccnt // (n-ccnt+1) + (0 if ccnt % (n-ccnt+1) == 0 else 1))
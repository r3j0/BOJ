import sys
input = sys.stdin.readline

x = input().rstrip()

if x[1] == 'x': print(int(x, 16))
elif x[0] == '0': print(int(x, 8))
else: print(x)
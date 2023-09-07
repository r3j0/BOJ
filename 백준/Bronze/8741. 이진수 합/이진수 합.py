import sys
input = sys.stdin.readline

n = int(input().rstrip())
print(bin((2**n-1)*(2**n)//2)[2:])
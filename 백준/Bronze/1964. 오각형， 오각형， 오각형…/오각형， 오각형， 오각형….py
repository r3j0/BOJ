import sys
input = sys.stdin.readline

n = int(input().rstrip())
print(((3*(n**2)+5*n)//2+1)%45678)
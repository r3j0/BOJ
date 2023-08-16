import sys
input = sys.stdin.readline

n = int(input().rstrip())
while str(n).count('4') + str(n).count('7') != len(str(n)):
    n -= 1

print(n)
import sys
input = sys.stdin.readline

c = input().rstrip()
print(abs(ord(c)-ord('I')) + 84)
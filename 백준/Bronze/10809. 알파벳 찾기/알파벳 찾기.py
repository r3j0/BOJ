import sys
input = sys.stdin.readline

s = input().rstrip()
for i in range(26):
    print(s.index(chr(ord('a') + i)) if s.find(chr(ord('a') + i)) != -1 else -1, end=' ')
import sys
input = sys.stdin.readline

s = input().rstrip()
k = input().rstrip()

for i in range(10):
    s = s.replace(chr(ord('0') + i), '')

if s.find(k) != -1: print(1)
else: print(0)
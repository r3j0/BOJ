import sys
input = sys.stdin.readline

n = int(input().rstrip())
string = input().rstrip()

ns = 0
ew = 0

for s in string:
    if s == 'N': ns += 1
    elif s == 'S': ns -= 1
    elif s == 'E': ew += 1
    elif s == 'W': ew -= 1

print(abs(ns) + abs(ew))
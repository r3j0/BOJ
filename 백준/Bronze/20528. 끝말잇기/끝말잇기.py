import sys
input = sys.stdin.readline

n = int(input().rstrip())

first_need = {}

strings = list(input().rstrip().split())
for s in strings:
    s = list(s)
    if first_need.get(s[0]):
        first_need[s[0]] += 1
    else:
        first_need[s[0]] = 1

if len(first_need) == 1: print(1)
else: print(0)
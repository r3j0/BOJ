import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

done = 0
while len(s) <= len(t):
    if s == t:
        done = 1
        break

    if t[-1] == 'A':
        del t[-1]
    else:
        del t[-1]
        t = t[::-1]

print(done)
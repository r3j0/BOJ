import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = 0
b = 0
for _ in range(n):
    aScore, bScore = map(int, input().rstrip().split())
    if aScore > bScore: a += 1
    elif aScore < bScore: b += 1

print(a, b)
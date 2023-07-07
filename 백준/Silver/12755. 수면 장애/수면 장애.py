import sys
input = sys.stdin.readline

n = int(input().rstrip())

now = 1
lens = 0
while lens + len(str(now)) < n:
    lens += len(str(now))
    now += 1

print(str(now)[n - lens - 1])
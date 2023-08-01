import sys
input = sys.stdin.readline

l = int(input().rstrip())
string = input().rstrip()

hashing = 0
for s in range(len(string)):
    hashing += (ord(string[s]) - ord('a') + 1) * (31**s)
    hashing = (hashing) % 1234567891

print(hashing)
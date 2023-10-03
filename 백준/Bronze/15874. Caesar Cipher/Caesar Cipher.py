import sys
input = sys.stdin.readline

k, s = map(int, input().rstrip().split())
string = input().rstrip()

for i in string:
    if 'A' <= i <= 'Z':
        print(chr((ord(i) - ord('A') + k) % 26 + ord('A')), end='')
    elif 'a' <= i <= 'z':
        print(chr((ord(i) - ord('a') + k) % 26 + ord('a')), end='')
    else: print(i, end='')
import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    a, b = map(int, input().rstrip().split())
    string = input().rstrip()

    for s in string:
        print(chr((a*(ord(s) - ord('A'))+b) % 26 + ord('A')), end='')
    print()
import sys
input = sys.stdin.readline

n, r, c = map(int, input().rstrip().split())
if (r + c) % 2 == 1:
    string = '.v'
    for _ in range(n):
        print(string*(n//2),end='')
        if n % 2 == 1:
            print(string[0])
        else:
            print()
        string = string[::-1]
else:
    string = 'v.'
    for _ in range(n):
        print(string*(n//2),end='')
        if n % 2 == 1:
            print(string[0])
        else:
            print()
        string = string[::-1]
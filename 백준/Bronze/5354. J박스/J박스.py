import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())

    print('#'*n)
    if n >= 2:
        if n >= 3:
            for _ in range(n-2):
                print('#' + 'J'*(n-2) + '#')
        print('#'*n)
    print()
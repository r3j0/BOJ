import sys
input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == 0: break

    string = list(input().rstrip())
    for i in range(n):
        idx = i
        mode = 0
        while (mode == 0 and idx < len(string)) or (mode == 1 and (idx - i + ((n-1) - i)) < len(string)):
            #print(string[idx if mode == 0 else (idx - (i+1) + (n - (i+1)))], idx)
            print(string[idx if mode == 0 else (idx - i + ((n-1) - i))], end='')
            idx += n
            mode = (1 if mode == 0 else 0)
    print()
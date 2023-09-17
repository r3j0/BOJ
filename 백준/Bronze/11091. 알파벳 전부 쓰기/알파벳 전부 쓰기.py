import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    string = input().rstrip().lower()
    arr = [0 for _ in range(26)]
    for s in string:
        if 'a' <= s <= 'z':
            arr[ord(s) - ord('a')] = 1
    
    if sum(arr) == 26: print('pangram')
    else:
        print('missing', end=' ')
        for i in range(26):
            if arr[i] == 0:
                print(chr(ord('a') + i), end='')
        print()
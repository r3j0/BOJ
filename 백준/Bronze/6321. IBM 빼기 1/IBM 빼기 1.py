import sys
input = sys.stdin.readline

t = int(input().rstrip())

for i in range(1, t+1):
    string = input().rstrip()

    print('String #%d'%i)
    for s in string:
        print(chr(((ord(s) - ord('A')) + 1) % 26 + ord('A')), end='')
    
    if i != t: print('\n')
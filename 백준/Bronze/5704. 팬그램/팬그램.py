import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '*': break

    arr = [0 for _ in range(26)]
    for s in string:
        if ord('a') <= ord(s) <= ord('z'):
            arr[ord(s) - ord('a')] = 1
    
    if sum(arr) == 26: print('Y')
    else: print('N')
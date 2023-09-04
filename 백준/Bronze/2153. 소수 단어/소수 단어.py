arr = [0 for _ in range(1050)]
arr[0] = 1
for i in range(2, 1050):
    j = 2
    while i * j < 1050:
        arr[i*j] = 1
        j += 1

import sys
input = sys.stdin.readline

string = input().rstrip()
sums = 0
for s in string:
    if 'a' <= s <= 'z':
        sums += ord(s) - ord('a') + 1
    else:
        sums += ord(s) - ord('A') + 27

if arr[sums] == 0: print('It is a prime word.')
else: print('It is not a prime word.')
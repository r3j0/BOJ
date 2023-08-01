import sys
input = sys.stdin.readline

arr = []
for i in range(5):
    string = input().rstrip()
    if 'FBI' in string: arr.append(i+1)

if len(arr) > 0: print(' '.join(map(str, arr)))
else: print('HE GOT AWAY!')
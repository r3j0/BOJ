import sys
input = sys.stdin.readline

alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

m, n = map(int, input().rstrip().split())
arr = []
for i in range(m, n+1):
    now = list(map(int, list(str(i))))
    now_str = ""
    for a in now:
        if len(now_str) == 0: 
            now_str = alpha[a]
        else:
            now_str += ' ' + alpha[a]
    
    arr.append([i, now_str])

arr.sort(key=lambda x:x[1])
for i in range(len(arr)):
    print(arr[i][0], end=' ')
    if i != 0 and (i + 1) % 10 == 0:
        print()
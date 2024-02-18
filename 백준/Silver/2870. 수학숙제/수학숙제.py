import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    string = input().rstrip()
    for i in range(26):
        string = string.replace(chr(ord('a') + i), ' ')
    now_arr = list(string.split())
    idx = 0
    while idx < len(now_arr):
        if now_arr[idx] == '':
            del now_arr[idx]
        else:
            now_arr[idx] = now_arr[idx].strip()
            idx += 1
    
    for na in now_arr:
        arr.append(int(na))

arr.sort()
for a in arr: print(a)

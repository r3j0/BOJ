import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = ['?' for _ in range(n)]
now = 0
done = True
for _ in range(k):
    s, c = input().rstrip().split()
    now = (now + int(s)) % n
    if (arr[now] == '?' and c not in arr) or (arr[now] == c):
        arr[now] = c
    else:
        done = False
arr = arr[::-1]
if done == False: print('!')
else:
    now = n - 1 - now
    while now != 0:
        go = arr[0]
        del arr[0]
        arr.append(go)
        now -= 1
    print(''.join(arr))
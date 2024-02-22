import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    arr = []
    while True:
        a = int(input().rstrip())
        if a == 0: break
        arr.append(a)
    
    arr.sort(reverse=True)
    res = 0
    for i in range(len(arr)):
        res += 2*(arr[i]**(i+1))
    if res <= 5*(10**6): print(res)
    else: print('Too expensive')
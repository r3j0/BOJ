import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().rstrip().split())
    if n == m == 0: break

    cnt = {}
    for _ in range(n):
        arr = list(map(int, input().rstrip().split()))
        for a in arr:
            if cnt.get(a, -1) == -1: cnt[a] = 1
            else: cnt[a] += 1
        
    answer = list(sorted(list(cnt.values()), reverse=True))[1]
    res = []
    for k, v in cnt.items():
        if v == answer: res.append(k)
    
    print(' '.join(map(str, sorted(res))))
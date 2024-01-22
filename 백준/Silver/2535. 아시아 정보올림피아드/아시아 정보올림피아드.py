import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
arr.sort(key = lambda x: -x[2])

country = [0 for _ in range(n+1)]
cnt = 0
for a in arr:
    if country[a[0]] != 2:
        country[a[0]] += 1

        print(a[0], a[1])
        cnt += 1
    
    if cnt == 3: break
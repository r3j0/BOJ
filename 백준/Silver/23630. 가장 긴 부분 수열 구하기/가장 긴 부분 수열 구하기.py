import sys
input = sys.stdin.readline

mask = [0 for _ in range(20)]
n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
for a in arr:
    now = a
    cnt = 0
    while now != 0:
        mask[cnt] += now % 2
        now >>= 1
        cnt += 1
    
print(max(mask))
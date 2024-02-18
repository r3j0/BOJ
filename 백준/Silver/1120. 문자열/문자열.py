import sys
input = sys.stdin.readline

a, b = input().rstrip().split()

max_cnt = -1
for i in range(len(b)-len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1

    if max_cnt == -1: max_cnt = cnt
    else: max_cnt = min(max_cnt, cnt)
print(max_cnt)
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split(',')))

def bgogo(lis):
    if len(lis) == 0: return lis

    new_lis = []
    for i in range(len(lis) - 1):
        new_lis.append(lis[i+1] - lis[i])
    return new_lis

for _ in range(k):
    arr = bgogo(arr)

print(','.join(map(str, arr)))
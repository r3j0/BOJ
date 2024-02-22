import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
cnt = 0
res = [-1]
n, k = map(int, input().rstrip().split())
def partition(arr, p, r):
    global cnt
    global res
    global k
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if (arr[j] <= x):
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            cnt += 1
            if cnt == k:
                res = []
                for a in arr:
                    res.append(a)
    if (i + 1 != r):
        tmp = arr[i+1]
        arr[i+1] = arr[r]
        arr[r] = tmp
        cnt += 1
        if cnt == k:
            res = []
            for a in arr:
                res.append(a)
    return i + 1

def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)


a = list(map(int, input().rstrip().split()))
quick_sort(a, 0, n-1)
print(' '.join(map(str, res)))
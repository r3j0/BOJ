import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    w = input().rstrip()
    k = int(input().rstrip())

    if k == 1: 
        print(1, 1)
    else:
        arr = [[] for _ in range(26)]
        for i in range(len(w)):
            arr[ord(w[i]) - ord('a')].append(i)
        
        min_size = -1
        max_size = -1
        for i in range(26):
            if len(arr[i]) < k: continue
            for j in range(k-1, len(arr[i])):
                if min_size == -1 or (min_size != -1 and arr[i][j] - arr[i][j - (k-1)] + 1 < min_size):
                    min_size = arr[i][j] - arr[i][j - (k-1)] + 1
                if max_size == -1 or (max_size != -1 and arr[i][j] - arr[i][j - (k-1)] + 1 > max_size):
                    max_size = arr[i][j] - arr[i][j - (k-1)] + 1

        if min_size == -1 or max_size == -1: print(-1)
        else: print(min_size, max_size)
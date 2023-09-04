import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    arr = [int(input().rstrip()) for _ in range(n)]

    min_value = max(arr) + 1
    for i in range(1, max(arr) + 1):
        dic = {}
        done = 0
        for k in range(n):
            if dic.get(arr[k] % i):
                done = 1
                break
            else:
                dic[arr[k] % i] = 1
        
        if done == 0:
            min_value = i
            break
    print(min_value)
import sys
input = sys.stdin.readline

n, c = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(n)]
if 1 in arr: print(c)
else:
    dic = {}
    for a in arr:
        idx = 1
        while a*idx <= c:
            dic[a*idx] = 1
            idx += 1
    
    print(len(dic))
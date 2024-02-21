import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [input().rstrip() for _ in range(n)]

result = ''
cnt = 0
for j in range(m):
    dic = {}
    for i in range(n):
        if dic.get(arr[i][j], -1) == -1:
            dic[arr[i][j]] = 1
        else:
            dic[arr[i][j]] += 1
        
    lis = list(dic.items())
    if len(lis) == 1:
        result += lis[-1][0]
    else:
        lis.sort(key=lambda x:(x[1], -ord(x[0])))
        result += lis[-1][0]
        cnt += n - lis[-1][1]

print(result)
print(cnt)
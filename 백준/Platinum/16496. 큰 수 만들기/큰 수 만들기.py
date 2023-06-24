import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().rstrip().split())
maxlen = 0
for a in arr: maxlen = max(maxlen, len(a))

lis = []
for a in range(n-1):
    maxs = a
    for b in range(a+1, n):
        idx = 0
        sa = list(arr[maxs])
        sb = list(arr[b])
        while idx < len(arr[maxs]) + 1 or idx < len(arr[b]) + 1:
            if sa == arr[b] or sb == arr[maxs]: 
                maxs = b
                break
            
            if (sa[idx] < sb[idx]):
                maxs = b
                break
            elif (sa[idx] > sb[idx]):
                break
            
            idx += 1
            if idx == len(sa): sa.extend(list(arr[maxs]))
            if idx == len(sb): sb.extend(list(arr[b]))
    
    if maxs != a:
        tmp = str(arr[a])
        arr[a] = str(arr[maxs])
        arr[maxs] = str(tmp)

result = ""
for a in arr:
    result += a

if result.count('0') == len(result): print(0)
else: print(result)
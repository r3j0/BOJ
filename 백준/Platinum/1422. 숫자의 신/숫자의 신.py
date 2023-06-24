import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = []
for _ in range(n): arr.append(input().rstrip())
maxlen = 0
for a in arr: maxlen = max(maxlen, len(a))
maxs = 0
for a in range(len(arr)):
    if len(arr[a]) == maxlen and int(arr[maxs]) < int(arr[a]):
        maxs = a

for _ in range(m-n): arr.append(arr[maxs])

for a in range(m-1):
    maxs = a
    for b in range(a+1, m):
        idx = 0
        sa = list(arr[maxs])
        sb = list(arr[b])
        if arr[maxs] == arr[b]: continue
        while idx < 2*len(arr[maxs]) or idx < 2*len(arr[b]):
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

print(result)
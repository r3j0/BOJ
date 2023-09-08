import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [input().rstrip() for _ in range(n)]

start = ''
end = ''
for i in range(n):
    if arr[i] == '?':
        if i > 0:
            start = arr[i-1][-1]
        if i < n - 1:
            end = arr[i+1][0]
        break

m = int(input().rstrip())
result = ''
for _ in range(m):
    tmp = input().rstrip()
    if result != '': continue
    if ((start != '' and start == tmp[0]) or start == '') and ((end != '' and end == tmp[-1]) or end == '') and (tmp not in arr):
        result = tmp
print(result)
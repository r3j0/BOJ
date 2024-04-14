""" 
# BS 풀이
import sys 
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort()
res = 0
for i in range(1, n):
    start = 0
    end = i - 1
    need = m - arr[i]
    if need > arr[end]: continue
    cnt = 0
    while cnt < 50 and start <= end:
        cnt += 1
        mid = (start + end) // 2
        if arr[mid] == need:
            res += 1
            break
        elif arr[mid] > need:
            end = mid - 1
        else:
            start = mid + 1
print(res) 
"""

import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
arr = list(map(int, input().rstrip().split())) 
arr.sort()

start = 0
end = n - 1
result = 0
while start < end:
    if arr[start] + arr[end] == m:
        result += 1
    
    if arr[start] + arr[end] >= m:
        end -= 1
    else:
        start += 1
        
print(result)
        
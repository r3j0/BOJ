import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(n)]

start = 0
end = max(arr)

def spls(m):
    global n
    if m == 0: return 0
    cnt = 0
    for i in range(n): cnt += arr[i] // m
    return cnt

while start < end:
    mid = (start + end) // 2
    cnt = spls(mid)
    #print(mid, cnt)

    if start == end - 1:
        #print(start, end)
        if spls(end) >= k:
            start = end
        else:
            end = start
        break
    else:
        if cnt >= k: # 나눴을 때 K명보다 많다면 : 용량 늘리기
            start = mid
        elif cnt < k: # 나눴을 떄 K명보다 작다면 : 더 적게 
            end = mid - 1

print(end)
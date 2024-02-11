import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(n)]

start = 1
end = max(arr)

def spls(m):
    global n
    if m == 0: return 0
    cnt = 0
    for i in range(n): cnt += arr[i] // m
    return cnt

res = 0
while start <= end:
    mid = (start + end) // 2
    cnt = spls(mid)

    if cnt >= k: # 나눴을 때 K명보다 많거나 같다면 : 찾을 용량 늘리기
        res = mid
        start = mid + 1
    elif cnt < k: # 나눴을 떄 K명보다 작다면 : 찾을 용량 줄이기
        end = mid - 1

print(end)
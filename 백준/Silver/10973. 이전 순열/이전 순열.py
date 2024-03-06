import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
# 오->왼 큰 쌍 찾았다? 그럼 오른쪽 배열에서 왼에 가까운 가장 큰 수 바꾸기 (그리고 역정렬)

if arr == sorted(arr): print(-1)
else:
    now = []
    for i in range(n-1, 0, -1):
        heapq.heappush(now, -arr[i])
        if arr[i-1] > arr[i]:
            go = []
            next = -heapq.heappop(now)
            while next > arr[i-1]: 
                go.append(next)
                next = -heapq.heappop(now)
            go.append(arr[i-1])
            arr[i-1] = next
            while now: go.append(-heapq.heappop(now))
            go.sort(reverse=True)
            print(' '.join(map(str, arr[:i] + go)))
            break
import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
if arr == sorted(arr, reverse=True): print(-1)
else:
    # 1 2 3 4 5
    # 1 2 3 5 4
    # 1 2 4 3 5
    # 1 2 4 5 3
    # 1 2 5 3 4
    # 1 2 5 4 3
    # 1 3 2 4 5
    # 오른쪽부터 순회. 작아지는걸 발견 ->
    # -> 그 오른쪽 전부 뒤집기, 작아지는 수에 가장 가까운 큰 수 가져오기
    for i in range(n-1, 0, -1):
        if arr[i-1] < arr[i]:
            queue = []
            for j in range(i, n):
                heapq.heappush(queue, arr[j])
            
            res = []
            while True:
                now = heapq.heappop(queue)
                if arr[i-1] < now:
                    heapq.heappush(queue, arr[i-1])
                    arr[i-1] = now
                    break
                else: res.append(now)
            while queue: res.append(heapq.heappop(queue))
            print(' '.join(map(str, arr[:i] + res)))
            break
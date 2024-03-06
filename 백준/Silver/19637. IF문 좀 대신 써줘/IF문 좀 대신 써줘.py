import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
first_arr = [list(input().rstrip().split()) for _ in range(n)]
arr = []
i = 0
size = len(first_arr)
while i < size:
    first_arr[i][1] = int(first_arr[i][1])
    if i == 0 or (i > 0 and first_arr[i][1] != first_arr[i-1][1]):
        arr.append(first_arr[i])
        
    i += 1

size = len(arr)
for _ in range(m):
    k = int(input().rstrip())
    start = 0
    end = size - 1
    if size == 1: print(arr[0][0])
    else:
        while start < end:
            if end - start == 1:
                #print(start, end)
                if arr[start][1] < k:
                    print(arr[end][0])
                else:
                    print(arr[start][0])
                break

            mid = (start + end) // 2
            if arr[mid][1] < k:
                start = mid + 1
            else:
                end = mid
        if end - start == 0:
            print(arr[start][0])
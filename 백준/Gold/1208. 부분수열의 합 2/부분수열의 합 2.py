import sys
input = sys.stdin.readline

n, s = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

arr_front = arr[:n//2]
arr_back = arr[n//2:]

sum_front = {}
sum_back = {}

def partialSequenceSum(arr, sum, now, start):
  arr_size = len(arr)
  for i in range(start+1, arr_size):
    if sum.get(now + arr[i], -1) == -1: sum[now + arr[i]] = 1
    else: sum[now + arr[i]] += 1
    partialSequenceSum(arr, sum, now + arr[i], i)

partialSequenceSum(arr_front,sum_front,0,-1)
partialSequenceSum(arr_back,sum_back,0,-1)

if sum_front.get(0, -1) == -1: sum_front[0] = 1
else: sum_front[0] += 1
if sum_back.get(0, -1) == -1: sum_back[0] = 1
else: sum_back[0] += 1

sum_back_key = list(sum_back.keys())
sum_back_key.sort()

def BinarySearch(key):
    global sum_back
    global sum_back_key
    start = 0
    end = len(sum_back_key) - 1

    while start <= end:
        mid = (start + end) // 2

        if sum_back_key[mid] == key: return sum_back[sum_back_key[mid]]
        if sum_back_key[mid] < key: start = mid + 1
        else: end = mid - 1
    return 0

result = 0
for k, v in sum_front.items():
    result += v * BinarySearch(s - k)

if s == 0: print(result - 1)
else: print(result)
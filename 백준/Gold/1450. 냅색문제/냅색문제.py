import sys
input = sys.stdin.readline

n, c = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

if n == 1:
    if arr[0] > c: print(1)
    else: print(2)
else:
    arr_first = arr[:n//2]
    arr_second = arr[n//2:]

    sum_first = [0]
    sum_second = [0]

    def PartialSum(sums, arrs, now, start):
        for i in range(start, len(arrs)):
            sums.append(now + arrs[i])
            PartialSum(sums, arrs, now + arrs[i], i+1)
    
    PartialSum(sum_first, arr_first, 0, 0)
    PartialSum(sum_second, arr_second, 0, 0)

    dic_first = {}
    dic_second = {}

    for sf in sum_first: 
        if dic_first.get(sf, -1) == -1: dic_first[sf] = 1
        else: dic_first[sf] += 1

    for ss in sum_second: 
        if dic_second.get(ss, -1) == -1: dic_second[ss] = 1
        else: dic_second[ss] += 1

    items_first = list(dic_first.items())
    items_first.sort(key=lambda x:x[0])
    dic_first = dict(items_first)

    items_second = list(dic_second.items())
    items_second.sort(key=lambda x:x[0])
    dic_second = dict(items_second)

    keys_first = list(dic_first.keys())
    keys_second = list(dic_second.keys())

    values_first = list(dic_first.values())
    values_second = list(dic_second.values())
    values_sum_first = [0]
    for v in values_first: values_sum_first.append(values_sum_first[-1] + v)
    values_sum_second = [0]
    for v in values_second: values_sum_second.append(values_sum_second[-1] + v)

    def BinarySearch(a, dest):
        start = 0
        end = len(a) - 1

        while start <= end:
            mid = (start + end) // 2
            if a[mid] == dest:
                return mid
            if a[mid] < dest:
                start = mid + 1
            else:
                end = mid - 1
        if len(a) == start: return len(a) - 1
        if a[start] > dest: return start - 1
        return start

    result = 0
    for kf in keys_first: 
        if c - kf < 0: continue
        result += dic_first[kf] * (values_sum_second[BinarySearch(keys_second, c - kf) + 1])

    print(result)
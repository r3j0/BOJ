import sys
input = sys.stdin.readline

# 머리 / 가슴 / 배
# 머리 < 배 < 가슴
# 1. y 하나 정해놓기
# 2. mid까지 누적 합 < y 정해 놓은 누적합 < y까지전체 합 - mid까지 누적 합 로 x 찾아서, 머리가 안 커질때까지의 개수를 정해놓기
n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
sums = [0]
for a in arr: sums.append(sums[-1] + a)
del sums[0]

result = 0
for y in range(1, n - 1):
    stomSum = sums[-1] - sums[y] # y 정해 놓은 누적합

    start = 0
    end = y - 1
    if start == end:
        #print('y', y, '->', sums[0], stomSum, sums[y] - sums[0])
        if sums[0] < stomSum < sums[y] - sums[0]: result += 1
    else:
        cnt = 0
        already = 0
        while start <= end:
            mid = (start + end) // 2
            #print('y', y, 'mid', mid, '->', sums[mid], stomSum, sums[y] - sums[mid])
            if sums[mid] < stomSum < sums[y] - sums[mid]:
                #print(mid + 1, already)
                result += mid + 1 - already
                already = mid + 1
                start = mid + 1
            else:
                end = mid - 1

print(result)
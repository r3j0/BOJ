import sys
input = sys.stdin.readline

k = int(input().rstrip())
for t in range(1, k+1):
    arr = list(map(int, input().rstrip().split()))

    nums = list(sorted(arr[1:]))

    largest_gap = 0
    for i in range(len(nums) - 1):
        largest_gap = max(largest_gap, nums[i+1] - nums[i])

    print('Class', t)
    print('Max %d, Min %d, Largest gap %d'%(max(arr[1:]), min(arr[1:]), largest_gap))
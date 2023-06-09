nums = []
for _ in range(4):
    nums.append(int(input().rstrip()))

if (nums[0] in [8, 9]) and nums[1] == nums[2] and (nums[3] in [8, 9]): print('ignore')
else: print('answer')
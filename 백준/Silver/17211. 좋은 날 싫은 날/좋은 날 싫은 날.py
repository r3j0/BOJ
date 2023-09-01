import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(float, input().rstrip().split()))
good = 0
bad = 0
if k == 0:
    good = 1
else:
    bad = 1

for _ in range(n):
    new_good = good * arr[0] + bad * arr[2]
    new_bad = good * arr[1] + bad * arr[3]

    good = new_good
    bad = new_bad

print('%.0f'%(good * 1000))
print('%.0f'%(bad * 1000))
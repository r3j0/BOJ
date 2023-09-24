import sys
input = sys.stdin.readline

n = int(input().rstrip())
res = sum(list(map(int, input().rstrip().split())))

if res > 0: print('Right')
elif res < 0: print('Left')
else: print('Stay')
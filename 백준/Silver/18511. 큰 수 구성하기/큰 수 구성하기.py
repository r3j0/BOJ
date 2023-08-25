import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

max_value = 0

def find_max_value(now):
    global max_value
    max_value = max(max_value, int(now) if now != '' else 0)
    for i in arr:
        nowstr = now + str(i)
        if int(nowstr) <= n:
            find_max_value(nowstr)

find_max_value('')
print(max_value)
import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().split())
dic = {}
for a in arr:
    if len(a) >= 6 and a[-6:] == 'Cheese':
        if len(a) == 6:
            if dic.get(0, -1) == -1:
                dic[0] = 1
            else:
                dic[0] += 1
        else:
            if dic.get(a[:-6], -1) == -1:
                dic[a[:-6]] = 1
            else:
                dic[a[:-6]] += 1

if len(dic) >= 4: print('yummy')
else: print('sad')
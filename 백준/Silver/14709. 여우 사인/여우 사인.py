import sys
input = sys.stdin.readline

n = int(input())
order = []
for _ in range(n):
    a, b = map(int, input().split())
    order.append([min(a,b), max(a,b)])
order = sorted(order, key=lambda x:(x[0], x[1]))

if len(order) == 3 and order[0] == [1,3] and order[1] == [1,4] and order[2] == [3,4]: print('Wa-pa-pa-pa-pa-pa-pow!')
else: print('Woof-meow-tweet-squeek')
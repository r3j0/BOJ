import sys
input = sys.stdin.readline

k, l = map(int, input().rstrip().split())
order = {}
for i in range(l):
    now = input().rstrip()
    order[now] = i

result = list(order.items())
result.sort(key = lambda x: x[1])
for i in range(min(k, len(result))): print(result[i][0])
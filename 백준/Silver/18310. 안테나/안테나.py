import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))

houses = {i:0 for i in range(1, 100001)}
now_dist = 0
max_a = 0
min_a = 100001
for a in arr: 
    min_a = min(min_a, a)
    max_a = max(max_a, a)
    houses[a] += 1
    now_dist += a-1

now = min_a
lefthouse = 0
nowhouse = houses[min_a]
righthouse = n - nowhouse

max_dist = now_dist
max_now = now
while now <= max_a:
    if now == min_a: 
        now += 1
        continue
    lefthouse += nowhouse
    nowhouse = houses[now]
    righthouse -= houses[now]

    now_dist += lefthouse
    now_dist -= nowhouse
    now_dist -= righthouse
    #print("left : %d now : %d right : %d"%(lefthouse,nowhouse,righthouse))
    #print("nowd : %d maxd : %d now : %d max : %d"%(now_dist, max_dist, now, max_now))

    if houses[now] > 0 and max_dist > now_dist:
        max_dist = now_dist
        max_now = now

    now += 1

print(max_now)
import sys
input = sys.stdin.readline

n = int(input().rstrip())
waiting = []
max_waiting_len = 0
max_waiting_last = 9999999
for _ in range(n):
    order = list(map(int, input().rstrip().split()))
    if order[0] == 1:
        waiting.append(order[1])
    else:
        del waiting[0]
    
    if (max_waiting_len < len(waiting)) or (max_waiting_len == len(waiting) and max_waiting_last > waiting[-1]):
        max_waiting_len = len(waiting)
        max_waiting_last = waiting[-1]

print(max_waiting_len, max_waiting_last)

import sys
input = sys.stdin.readline

v = int(input().rstrip())
graph = [{} for _ in range(v+1)] 
for _ in range(v):
    order = list(map(int, input().rstrip().split()))
    idx = 1
    while order[idx] != -1:
        graph[order[0]][order[idx]] = order[idx+1]
        idx += 2

def find_longest(now):
    max_value = 0
    max_key = now
    for key, value in graph[now].items():
        if visited_fl[key] == 0:
            visited_fl[key] = 1
            res = find_longest(key)
            now_value = value + res[1]
            if now_value > max_value:
                max_value = now_value
                max_key = res[0]
    return (max_key, max_value)    
    
visited_fl = [0 for _ in range(v+1)]
visited_fl[1] = 1
start = find_longest(1)

visited_fl = [0 for _ in range(v+1)]
visited_fl[start[0]] = 1
print(find_longest(start[0])[1])
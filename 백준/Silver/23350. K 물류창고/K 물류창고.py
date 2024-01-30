import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 컨테이너는 레일을 통해 하나씩 오고, 우선순위가 낮은 컨테이너를 먼저 적재한다. 
# 낮은 우선순위의 컨테이너들이 모두 적재되지 않은 상태에서 높은 우선순위의 
# 컨테이너가 온다면 레일의 처음으로 보낸다. 레일의 처음으로 보낼 때, 
# 컨테이너의 무게만큼 비용이 발생한다. 낮은 우선순위의 컨테이너가 온다면, 무조건 적재한다.

# -> 우선순위마다 갯수 세서 배열로 만들어 진행

# 컨테이너의 우선순위가 같을 땐, 무게가 무거운 컨테이너를 아래에 위치시킨다. 우선순위는 같으나, 
# 무게가 가벼운 컨테이너가 먼저 적재돼 있을 경우, 가벼운 컨테이너가 무거운 컨테이너 위로 갈 수 있도록 
# 컨테이너를 빼내고 다시 적재한다. 이 과정을, 가벼운 컨테이너가 모두 빠질 때까지 반복한다. 
# 이 과정에서 컨테이너를 뺄 때와 적재될 때 컨테이너의 무게만큼 비용이 발생한다.

# -> 적재 공간을 스택으로 만들어서 진행

queue = deque()
priority_dict = {}

for a in arr:
    if priority_dict.get(a[0], -1) == -1: priority_dict[a[0]] = 1 
    else: priority_dict[a[0]] += 1 
    queue.append(a)

priority_list = list(priority_dict.items())
for p in range(len(priority_list)): priority_list[p] = list(priority_list[p])
priority_list.sort(key=lambda x:-x[0])

result_stack = []
last_stack = []
cost = 0

while queue:
    now = queue.popleft()
    if priority_list[0][0] == now[0]:
        # 적재
        while len(result_stack) > 0 and result_stack[-1][0] == now[0] and result_stack[-1][1] < now[1]:
            go = result_stack.pop()
            cost += go[1]
            last_stack.append(go) 
        result_stack.append(now)
        cost += now[1]
        while last_stack:
            go = last_stack.pop()
            cost += go[1]
            result_stack.append(go)
        
        priority_list[0][1] -= 1
        if priority_list[0][1] == 0:
            del priority_list[0]
    else:
        # 적재 안함
        queue.append(now)
        cost += now[1]

print(cost)
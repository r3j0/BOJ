import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

homes = []
chickens = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1: homes.append([i, j])
        elif maps[i][j] == 2: chickens.append([i, j])

home_dict = {}
for i in range(len(homes)): home_dict[i] = -1

result = -1

def chickenGo(now, start, hd):
    global chickens
    global result
    global m

    if len(now) == m:
        #print(now)
        #print(hd)
        if result == -1: result = sum(list(hd.values()))
        else: result = min(result, sum(list(hd.values())))
        #print(sum(list(hd.values())))
        return

    for i in range(start, len(chickens)):
        #print(hd)
        new_hd = {}
        for k, v in hd.items(): new_hd[k] = v

        for k in range(len(new_hd)):
            if new_hd[k] == -1: new_hd[k] = abs(homes[k][0] - chickens[i][0]) + abs(homes[k][1] - chickens[i][1])
            else:
                new_hd[k] = min(new_hd[k], abs(homes[k][0] - chickens[i][0]) + abs(homes[k][1] - chickens[i][1]))

        now.append(i)
        chickenGo(now, i + 1, new_hd)
        now.pop()


chickenGo([], 0, home_dict)
print(result)
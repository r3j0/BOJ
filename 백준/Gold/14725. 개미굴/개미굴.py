import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = {0:['ROOT', []]}

def insertNode(arr, nownode):
    find = -1
    for i in graph[nownode][1]:
        if graph[i][0] == arr[0]:
            find = i
            break
    
    if find == -1:
        graph[len(graph)] = [arr[0], []]
        graph[nownode][1].append(len(graph)-1)
        if len(arr) == 1: return
        insertNode(arr[1:], len(graph)-1)
    else:
        insertNode(arr[1:], find)

for _ in range(n):
    order = list(input().rstrip().split())[1:]
    insertNode(order, 0)

for k, v in graph.items():
    if len(v[1]) > 0:
        graph[k][1].sort(key = lambda x:graph[x][0])

def findNode(nownode, depth):
    if nownode != 0:
        print(('--'*depth) + graph[nownode][0])
    if len(graph[nownode][1]) > 0:
        for i in graph[nownode][1]:
            findNode(i, depth+1)

findNode(0, -1)
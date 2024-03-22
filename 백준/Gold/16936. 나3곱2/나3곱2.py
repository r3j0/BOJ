import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort()

# 1. 이중 반복문으로 2배 쌍 찾기
vis = [0 for _ in range(n)]

dic = {}
for i in range(1, n):
    for j in range(i):
        if arr[j] * 2 == arr[i]:
            if dic.get(arr[j], -1) == -1:
                dic[arr[i]] = [arr[j], arr[i]]
                vis[i] = 1
                vis[j] = 1
            else:
                go = dic[arr[j]]
                del dic[arr[j]]
                go.append(arr[i])
                dic[arr[i]] = go
                vis[i] = 1

# 2. 남은 걸로 나누기 3 쌍 찾기
node = []
for i in range(n):
    if vis[i] == 0:
        node.append([arr[i]])
for v in dic.values():
    node.append(v)

edge = [-1 for _ in range(len(node))]

for i in range(len(node)):
    for j in range(len(node)):
        if i == j: continue

        if node[i][-1] % 3 == 0 and node[i][-1] // 3 == node[j][0]:
            edge[i] = j

# 3. 루트 찾기
root = -1
for i in range(len(node)):
    if edge.count(i) == 0:
        root = i
        break

while root != -1:
    for a in node[root]:
        print(a, end=' ')
    root = edge[root]
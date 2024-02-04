import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    parent = {}
    network = {}

    def parentSearch(now):
        if now != parent[now]:
            go = parentSearch(parent[now])
            parent[now] = go
            return go
        return now

    def union(p1, p2):
        p1 = parentSearch(p1)
        p2 = parentSearch(p2)

        if p1 != p2:
            parent[p2] = p1
            network[p1] += network[p2]
        return p1

    for _ in range(n):
        a, b = input().rstrip().split()
        if parent.get(a, -1) == -1 and parent.get(b, -1) == -1:
            parent[a] = a
            parent[b] = a
            network[a] = 2

            print(2)
        else:
            if parent.get(a, -1) == -1: 
                parent[a] = a
                network[a] = 1
            if parent.get(b, -1) == -1:
                parent[b] = b
                network[b] = 1
            
            print(network[union(a, b)])
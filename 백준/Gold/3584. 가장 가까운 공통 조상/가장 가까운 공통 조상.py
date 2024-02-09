import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    tree = [[] for _ in range(n+1)]
    parent = [-1 for _ in range(n+1)]

    for _ in range(n-1):
        a, b = map(int, input().rstrip().split())
        tree[a].append(b)
        parent[b] = a
    
    parent[0] = 0
    root = parent.index(-1)

    order = list(map(int, input().rstrip().split()))
    
    def findAnscestor(now):
        if now in order:
            return now
        
        if len(tree[now]) == 0:
            return -1
        
        child_value = 0
        child_cnt = 0
        for next in tree[now]:
            result = findAnscestor(next)
            if result != -1:
                child_value = result
                child_cnt += 1
        
        if child_cnt == 0: 
            return -1
        elif child_cnt == 1:
            return child_value
        else:
            return now 

    print(findAnscestor(root))
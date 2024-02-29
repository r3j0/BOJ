import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    clothes = {}
    for _ in range(n):
        name, type = input().rstrip().split()
    
        if not clothes.get(type):
            clothes[type] = ['/none/']
        clothes[type].append(name)

    res = 1
    for ck in list(clothes.keys()):
        res *= len(clothes[ck])
    print(res-1)
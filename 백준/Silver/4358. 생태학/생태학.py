import sys
input = sys.stdin.readline

trees = {}
cnt = 0
while True:
    tree = input().rstrip()
    if tree == '': break
    if trees.get(tree, -1) == -1: trees[tree] = 1
    else: trees[tree] += 1
    cnt += 1

result = list(trees.items())
result.sort(key=lambda x:x[0])

for r in result:
    print(r[0], '%.4f'%(r[1]/cnt*100))
import sys
from collections import deque
input = sys.stdin.readline

n, word = input().rstrip().split()
n = int(n)
words = [[] for _ in range(81)]
for _ in range(n):
    go = input().rstrip()
    words[len(go)].append(go)

queue = deque()
queue.append(word)
vis = {}
vis[word] = 1

result = word

def goWord(dest, src):
    for k in range(len(src)):
        cnt = 0
        idx = 0
        for j in range(len(src)):
            if k == j: continue
            if dest[idx] == src[j]: cnt += 1
            idx += 1
        
        if cnt == len(dest): return True
    return False

while queue:
    now = queue.popleft()
    if len(now) > len(result): result = now

    for i in range(len(words[len(now)+1])):
        if ((vis.get(words[len(now)+1][i]) and vis[words[len(now)+1][i]] == 0) or (not vis.get(words[len(now)+1][i]))) and goWord(now, words[len(now)+1][i]):
            vis[words[len(now)+1][i]] = 1
            queue.append(words[len(now)+1][i])

print(result)